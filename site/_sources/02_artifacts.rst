.. the actual IEC 61508 artifacts as Sphinx-needs objects

Lifecycle Artifacts
===================

This section encodes a minimal IEC 61508 SIL 2 lifecycle thread for an Emergency Stop function
as structured Sphinx-Needs artifacts.

Hazard
------

.. hazard:: Emergency Stop does not remove hazardous energy
   :id: HAZ_ESTOP_01
   :phase: Hazard and Risk Analysis
   :owner_role: Safety Engineer
   :part_ref: IEC 61508-1 (Hazard and Risk Analysis)

   If the Emergency Stop request is not effective, the machine may continue hazardous motion,
   exposing personnel to injury.

Risk Assessment
---------------

.. risk:: Risk of injury due to ineffective Emergency Stop
   :id: RISK_ESTOP_01
   :phase: Hazard and Risk Analysis
   :owner_role: Safety Engineer
   :part_ref: IEC 61508-1 (Risk Assessment)
   :addresses: HAZ_ESTOP_01

   Risk evaluation indicates that risk reduction is required for the Emergency Stop function.

SIL Allocation
--------------

.. sil:: SIL 2 allocated for Emergency Stop safety function
   :id: SIL_ESTOP_01
   :phase: Safety Function Allocation
   :owner_role: Functional Safety Manager
   :sil_level: SIL2
   :part_ref: IEC 61508-1 (SIL Allocation)
   :allocates: RISK_ESTOP_01

   Based on the risk assessment, the Emergency Stop safety function is allocated SIL 2.

Functional Safety Requirement
-----------------------------

.. fsr:: Emergency Stop shall de-energize motor outputs within 100 ms
   :id: FSR_ESTOP_01
   :phase: Safety Requirements Specification
   :owner_role: System Engineer
   :sil_level: SIL2
   :part_ref: IEC 61508-2 (SRS)
   :refines: SIL_ESTOP_01

   When the Emergency Stop is activated, the system shall remove power from motor outputs
   within 100 ms.

Technical Safety Requirement
----------------------------

.. tsr:: Dual-channel Emergency Stop input with discrepancy detection
   :id: TSR_ESTOP_01
   :phase: Safety Requirements Specification
   :owner_role: Hardware Engineer
   :sil_level: SIL2
   :part_ref: IEC 61508-2 (SRS)
   :refines: FSR_ESTOP_01

   The Emergency Stop shall be implemented with two independent input channels
   and discrepancy detection to detect wiring or contact faults.

Safety Architecture
-------------------

.. arch:: 1oo2 input evaluation and safety relay output stage
   :id: ARCH_ESTOP_01
   :phase: Architectural Design
   :owner_role: System Architect
   :part_ref: IEC 61508-2 (Architecture)
   :realizes: TSR_ESTOP_01

   The architecture evaluates both input channels and commands a safety relay / safe output stage
   to remove motor power.

Verification Activity
---------------------

.. verif:: Measure Emergency Stop response time
   :id: VERIF_ESTOP_01
   :phase: Verification
   :owner_role: Test Engineer
   :part_ref: IEC 61508-3 (Verification)
   :verifies: FSR_ESTOP_01

   Verification confirms the response time from Emergency Stop activation to output de-energization.

Evidence
--------

.. evidence:: Emergency Stop response time test report
   :id: EVID_ESTOP_01
   :phase: Verification Evidence
   :owner_role: Test Engineer
   :artifact_kind: Test Report
   :evidences: VERIF_ESTOP_01

   Evidence artifact documenting the measured response time and acceptance criteria.

Confirmation Measure
--------------------

.. confirm:: Independent review of SIL allocation and safety requirements
   :id: CONF_ESTOP_01
   :phase: Functional Safety Assessment
   :owner_role: Independent Assessor
   :part_ref: IEC 61508-1 (Confirmation Measures)
   :reviews: SIL_ESTOP_01

   Confirmation activity records independent review of the SIL allocation decision
   and the derived safety requirements.