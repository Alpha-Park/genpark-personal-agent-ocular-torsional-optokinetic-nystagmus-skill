# Ocular Optokinetic Nystagmus (OKN) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Optokinetic Nystagmus (OKN) slow-phase velocity gain, retinal slip velocity, and visual-vestibular motion stabilization.

```mermaid
flowchart TD
    LargeFieldMotion["Full-Field Visual Motion Drift (20-60 deg/s)"] --> NOT_AOS["Nucleus of the Optic Tract (NOT) & Accessory Optic System"]
    NOT_AOS --> SlowPhase["Slow-Phase Eye Smooth Pursuit Velocity (Vslow)"]
    SlowPhase --> RetinalSlip["Retinal Slip Velocity (Vstim - Vslow)"]
    NOT_AOS --> FastPhaseReset["Saccadic Fast-Phase Reset Beats (1.8-3.5 Hz)"]
    RetinalSlip & FastPhaseReset --> OKNScore["Optokinetic Gain & Visual Motion Sickness Engine"]
    OKNScore --> Agent["OpenClaw / Hermes Personal Agent UI Animation Moderation"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Visual Neurophysiology Standards**: Formulates OKN slow-phase gain, retinal slip speed, and directional symmetry ratios.
- **Screen Vertigo & Simulator Sickness Shield**: Detects early breakdown of wide-field visual tracking during rapid desktop screen interaction.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import OcularOptokineticNystagmusClient

client = OcularOptokineticNystagmusClient()
result = client.evaluate_okn(
    stimulus_velocity_deg_s=30.0,
    slow_phase_velocity_deg_s=27.2,
    fast_phase_frequency_hz=2.6
)
print("OKN Gain:", result["okn_gain"])
print("Optokinetic Score:", result["optokinetic_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
