---
name: genpark-personal-agent-ocular-torsional-optokinetic-nystagmus-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Optokinetic Nystagmus (OKN) slow-phase tracking gain, retinal slip velocity, and visual-vestibular motion stabilization.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Ocular Optokinetic Nystagmus (OKN) Skill

A sovereign personal agent capability for evaluating visual-vestibular interaction, subcortical optokinetic reflex pathways, slow-phase tracking gain ($Gain = V_{slow} / V_{stim}$), fast-phase saccadic reset frequency, and visual vertigo / simulator sickness.

## Core Capabilities
- **OKN Slow-Phase Velocity Gain**: Formulates tracking accuracy ($V_{slow} / V_{stim}$, normative: $0.78 - 0.98$) across wide-field visual motion.
- **Retinal Slip Velocity Quantification**: Calculates residual blur velocity ($\text{Slip} = V_{stim} - V_{slow}$ in $\text{deg/s}$).
- **Directional Tracking Symmetry**: Evaluates hemispheric balance between rightward and leftward optokinetic flow.
- **Visual Motion Sickness Prevention**: Automatically reduces UI parallax animations, dampens dynamic backgrounds, and prescribes gaze anchoring during fast data scrolling.

## Fast Invocation
```python
from client import OcularOptokineticNystagmusClient

client = OcularOptokineticNystagmusClient()
res = client.evaluate_okn(
    stimulus_velocity_deg_s=30.0,
    slow_phase_velocity_deg_s=27.2,
    fast_phase_frequency_hz=2.6
)
print("OKN Gain:", res["okn_gain"])
print("Optokinetic Score:", res["optokinetic_score"], "/ 100")
```
