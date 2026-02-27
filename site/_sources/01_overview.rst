.. what the demo is, how to build, what it shows

Overview
========

This demo shows how a minimal IEC 61508 safety lifecycle thread can be represented as structured,
traceable engineering artifacts using Sphinx and Sphinx-Needs. The example thread models a SIL 2
Emergency Stop safety function, from hazard and risk assessment through SIL allocation, requirements,
architecture, verification, and evidence.

Scope of the demo
-----------------

The documentation contains a single, end-to-end lifecycle thread:

- Hazard identification and risk assessment for an Emergency Stop function
- SIL allocation (target: SIL 2)
- Functional and technical safety requirements
- A minimal safety architecture
- Verification activities and linked evidence artifacts
- Traceability views and lifecycle completeness checks

Lifecycle view
--------------

.. figure:: _static/iec61508_workflow.svg
   :alt: IEC 61508 lifecycle workflow view used in the demo.
   :width: 95%

   IEC 61508 lifecycle overview used as the narrative structure for the SIL 2 Emergency Stop thread.