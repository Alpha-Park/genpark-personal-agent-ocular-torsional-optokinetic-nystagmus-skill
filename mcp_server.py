"""
MCP Server for Ocular Optokinetic Nystagmus (OKN) Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating OKN slow-phase gain, fast-phase frequency, and visual-motion scores.
"""

import sys
import json
from typing import Dict, Any
from client import OcularOptokineticNystagmusClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_okn",
                "description": "Calculates Optokinetic Nystagmus (OKN) slow-phase velocity gain, retinal slip (deg/s), reset frequency, and visual-motion stabilization score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "stimulus_velocity_deg_s": {
                            "type": "number",
                            "description": "Full-field visual stripe stimulus velocity in degrees per second (e.g. 30.0 deg/s, 45.0 deg/s)."
                        },
                        "slow_phase_velocity_deg_s": {
                            "type": "number",
                            "description": "Mean slow-phase eye tracking velocity in degrees per second (e.g. 26.5 deg/s)."
                        },
                        "fast_phase_frequency_hz": {
                            "type": "number",
                            "description": "Frequency of saccadic fast-phase reset beats in Hz (e.g. 2.6 Hz, normative 1.8-3.5 Hz)."
                        },
                        "directional_asymmetry_pct": {
                            "type": "number",
                            "description": "Percentage asymmetry between rightward and leftward tracking gain (normative < 15.0%, default: 6.0%).",
                            "default": 6.0
                        }
                    },
                    "required": ["stimulus_velocity_deg_s", "slow_phase_velocity_deg_s", "fast_phase_frequency_hz"]
                }
            }
        ]
    }


def handle_request(client: OcularOptokineticNystagmusClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_okn":
            asym = args.get("directional_asymmetry_pct")
            res = client.evaluate_okn(
                stimulus_velocity_deg_s=float(args.get("stimulus_velocity_deg_s", 30.0)),
                slow_phase_velocity_deg_s=float(args.get("slow_phase_velocity_deg_s", 26.0)),
                fast_phase_frequency_hz=float(args.get("fast_phase_frequency_hz", 2.5)),
                directional_asymmetry_pct=float(asym) if asym is not None else 6.0
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = OcularOptokineticNystagmusClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
