"""
Example Usage: Ocular Optokinetic Nystagmus (OKN) & Visual-Vestibular Motion Engine.
Demonstrates zero-dependency calculation of OKN slow-phase gain, retinal slip velocity, and visual-motion stabilization scoring.
"""

from client import OcularOptokineticNystagmusClient


def main():
    client = OcularOptokineticNystagmusClient()
    print("=== Ocular Optokinetic Nystagmus (OKN) Demo ===")

    # Test Case 1: Healthy vigorous optokinetic response (30 deg/s stimulus)
    res1 = client.evaluate_okn(
        stimulus_velocity_deg_s=30.0,
        slow_phase_velocity_deg_s=27.2,
        fast_phase_frequency_hz=2.6,
        directional_asymmetry_pct=5.2
    )
    print("\nTest Case 1: Optimal Optokinetic Tracking (30 deg/s)")
    print(f"  Stimulus Velocity: {res1['stimulus_velocity_deg_s']} deg/s | Slow Phase Eye Velocity: {res1['slow_phase_velocity_deg_s']} deg/s")
    print(f"  OKN Gain: {res1['okn_gain']} | Retinal Slip: {res1['retinal_slip_deg_s']} deg/s")
    print(f"  Fast-Phase Frequency: {res1['fast_phase_frequency_hz']} Hz | Asymmetry: {res1['directional_asymmetry_pct']}%")
    print(f"  Optokinetic Score: {res1['optokinetic_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Blunted OKN gain / elevated motion sickness risk
    res2 = client.evaluate_okn(
        stimulus_velocity_deg_s=45.0,
        slow_phase_velocity_deg_s=26.0,
        fast_phase_frequency_hz=1.4,
        directional_asymmetry_pct=22.0
    )
    print("\nTest Case 2: Deficient OKN Gain Pattern (Motion Sickness Vulnerability)")
    print(f"  OKN Gain: {res2['okn_gain']} | Retinal Slip: {res2['retinal_slip_deg_s']} deg/s")
    print(f"  Optokinetic Score: {res2['optokinetic_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
