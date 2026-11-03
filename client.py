"""
Ocular Optokinetic Nystagmus (OKN) & Visual-Vestibular Motion Engine.
Provides deterministic, zero-dependency modeling of optokinetic slow-phase tracking gain (V_slow / V_stim),
fast-phase reset frequency (Hz), directional asymmetry (%), and subcortical visual motion processing.
"""

from typing import Dict, Any, List, Optional


class OcularOptokineticNystagmusClient:
    """
    Deterministic client for calculating Optokinetic Nystagmus (OKN) dynamics.
    Assesses subcortical nucleus of the optic tract (NOT), accessory optic system (AOS),
    cortical middle temporal (MT/V5) visual flow processing, and visual-vestibular motion sickness.
    """

    def __init__(self):
        pass

    def evaluate_okn(
        self,
        stimulus_velocity_deg_s: float,
        slow_phase_velocity_deg_s: float,
        fast_phase_frequency_hz: float,
        directional_asymmetry_pct: Optional[float] = 6.0
    ) -> Dict[str, Any]:
        """
        Calculates OKN gain (slow_phase_vel / stimulus_vel) and visual motion score.
        Normative values (for stimulus velocity 20 - 60 deg/s):
        - OKN Gain: 0.78 - 0.98
        - Fast-phase frequency: 1.8 - 3.5 Hz
        - Directional asymmetry: < 15.0%
        """
        if stimulus_velocity_deg_s <= 0 or slow_phase_velocity_deg_s <= 0 or fast_phase_frequency_hz <= 0:
            return {"error": "Velocities and frequency must be strictly positive"}
        if slow_phase_velocity_deg_s > stimulus_velocity_deg_s * 1.3:
            return {"error": "Slow phase eye velocity cannot unrealistically exceed stimulus velocity"}

        # 1. OKN Slow-Phase Gain
        okn_gain = round(slow_phase_velocity_deg_s / stimulus_velocity_deg_s, 2)

        # 2. Retinal Slip Velocity (deg/s)
        retinal_slip_deg_s = round(stimulus_velocity_deg_s - slow_phase_velocity_deg_s, 1)

        # 3. Visual-Vestibular Optokinetic Score (0 - 100)
        score = 80.0
        if 0.82 <= okn_gain <= 0.98:
            score += 12.0
        elif 0.74 <= okn_gain < 0.82 or 0.98 < okn_gain <= 1.05:
            score += 5.0
        elif okn_gain < 0.55:
            score -= 30.0  # Profound optokinetic failure
        elif okn_gain < 0.70:
            score -= 15.0

        if 2.0 <= fast_phase_frequency_hz <= 3.5:
            score += 5.0
        elif fast_phase_frequency_hz < 1.2:
            score -= 15.0  # Sluggish saccadic reset

        if directional_asymmetry_pct is not None:
            if directional_asymmetry_pct <= 12.0:
                score += 5.0
            elif directional_asymmetry_pct > 25.0:
                score -= 20.0
            elif directional_asymmetry_pct > 18.0:
                score -= 10.0

        okn_score = round(min(100.0, max(5.0, score)), 1)

        if okn_score >= 85.0 and okn_gain >= 0.80 and (directional_asymmetry_pct is None or directional_asymmetry_pct <= 15.0):
            tier = "OPTIMAL_OPTOKINETIC_NYSTAGMUS_GAIN"
            interp = f"Robust optokinetic tracking (Gain {okn_gain}, Fast-phase {fast_phase_frequency_hz} Hz, Slip {retinal_slip_deg_s} deg/s); intact subcortical NOT/AOS motion pathways."
            guidance = "Superior large-field visual motion stabilization. Low susceptibility to visual vertigo and simulator sickness."
        elif okn_gain < 0.65:
            tier = "DEFICIENT_OPTOKINETIC_SLOW_PHASE_GAIN"
            interp = f"Markedly impaired OKN gain ({okn_gain} < 0.75, Slip {retinal_slip_deg_s} deg/s); reflects subcortical motion pathway fatigue or parieto-occipital cortical deficit."
            guidance = "Visual motion tracking impairment detected. Susceptible to scrolling motion sickness and screen vertigo; restrict dynamic background animations."
        elif directional_asymmetry_pct is not None and directional_asymmetry_pct > 20.0:
            tier = "ASYMMETRIC_OPTOKINETIC_RESPONSE"
            interp = f"Directional OKN asymmetry ({directional_asymmetry_pct}% > 15%); indicates unilateral cortical or cerebellar hemispheric tracking imbalance."
            guidance = "Asymmetric visual tracking. Screen for unilateral inner ear dysfunction or asymmetric cervical neck tension."
        else:
            tier = "MODERATE_OPTOKINETIC_COMPENSATION"
            interp = f"Moderate optokinetic gain ({okn_gain}, Retinal slip {retinal_slip_deg_s} deg/s); acceptable visual stabilization."
            guidance = "Adequate motion processing. Maintain steady gaze anchoring during fast-scrolling documents."

        return {
            "stimulus_velocity_deg_s": stimulus_velocity_deg_s,
            "slow_phase_velocity_deg_s": slow_phase_velocity_deg_s,
            "okn_gain": okn_gain,
            "retinal_slip_deg_s": retinal_slip_deg_s,
            "fast_phase_frequency_hz": fast_phase_frequency_hz,
            "directional_asymmetry_pct": directional_asymmetry_pct,
            "optokinetic_score": okn_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
