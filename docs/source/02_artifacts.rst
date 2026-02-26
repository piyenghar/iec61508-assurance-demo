.. the actual IEC 61508 artifacts as Sphinx-needs objects

Artifacts
=========

Concept Evidence
----------------

.. evidence:: Safety Plan Record
   :id: EVID-PLAN-01
   :phase: concept
   :owner_role: safety_manager
   :artifact_kind: plan_record
   :part_ref: IEC61508-1

   Defines lifecycle planning and assigned responsibilities.

Hazard Identification
---------------------

.. hazard:: Loss of emergency stop function
   :id: HZ-01
   :phase: hazard_risk
   :sil_level: SIL2
   :owner_role: safety_manager
   :part_ref: IEC61508-1

   Failure to remove actuator power in time.

Risk Assessment
---------------

.. risk:: Risk estimation for HZ-01
   :id: RISK-01
   :phase: hazard_risk
   :sil_level: SIL2
   :owner_role: safety_manager
   :addresses: HZ-01
   :part_ref: IEC61508-1

   Risk requires SIL2 reduction.

SIL Allocation
--------------

.. sil:: SIL2 allocation for E-stop
   :id: SIL-01
   :phase: hazard_risk
   :sil_level: SIL2
   :owner_role: safety_manager
   :allocates: RISK-01
   :part_ref: IEC61508-1

   SIL2 justified by risk analysis.

Functional Safety Requirement
-----------------------------

.. fsr:: E-stop shall remove power within 200 ms
   :id: FSR-01
   :phase: safety_requirements
   :sil_level: SIL2
   :owner_role: safety_manager
   :mitigates: HZ-01
   :part_ref: IEC61508-1

   Timing requirement for safety function.

Technical Safety Requirement
----------------------------

.. tsr:: Dual-channel E-stop input with discrepancy monitoring
   :id: TSR-01
   :phase: design_realization
   :sil_level: SIL2
   :owner_role: developer
   :refines: FSR-01
   :part_ref: IEC61508-2

   Hardware realization constraint.

Architecture
------------

.. arch:: Safety relay with monitored inputs
   :id: ARCH-01
   :phase: design_realization
   :sil_level: SIL2
   :owner_role: developer
   :realizes: TSR-01
   :part_ref: IEC61508-2

   Architecture for E-stop safety function.

Verification
------------

.. verif:: Measure E-stop response time
   :id: VER-01
   :phase: verification
   :sil_level: SIL2
   :owner_role: verifier
   :verifies: FSR-01
   :part_ref: IEC61508-3

   Bench test of response time.

.. evidence:: Test report for VER-01
   :id: EVID-01
   :phase: verification
   :owner_role: verifier
   :produces: VER-01
   :artifact_kind: test_report
   :part_ref: IEC61508-3

   Measured response times documented.

Confirmation
------------

.. confirm:: Independent review of safety requirements
   :id: CM-01
   :phase: safety_requirements
   :sil_level: SIL2
   :owner_role: assessor
   :reviews: FSR-01
   :part_ref: IEC61508-1

   Confirms adequacy of safety requirements.