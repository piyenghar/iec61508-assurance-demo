Lifecycle Checks
================

This section defines simple, automated completeness checks for the SIL 2 Emergency Stop thread.
The goal is to detect missing lifecycle links early (e.g., requirements without verification).

Check 1: Every FSR must be verified
-----------------------------------

Expected rule:
Each Functional Safety Requirement (FSR) shall have at least one incoming ``verified_by`` link
from a verification activity.

.. needtable::
   :types: fsr
   :filter: "'verified_by' not in links_back or len(links_back['verified_by']) == 0"
   :columns: id;title;sil_level;owner_role
   :sort_by: id

If this table is non-empty, verification coverage is incomplete.

Check 2: Every verification must have evidence
----------------------------------------------

Expected rule:
Each verification activity shall have at least one incoming ``evidenced_by`` link
from an evidence artifact.

.. needtable::
   :types: verif
   :filter: "'evidenced_by' not in links_back or len(links_back['evidenced_by']) == 0"
   :columns: id;title;owner_role
   :sort_by: id

If this table is non-empty, evidence coverage is incomplete.

Check 3: Every risk item must have a SIL allocation
---------------------------------------------------

Expected rule:
Each risk assessment entry shall have at least one incoming ``allocated_by`` link
from a SIL allocation artifact.

.. needtable::
   :types: risk
   :filter: "'allocated_by' not in links_back or len(links_back['allocated_by']) == 0"
   :columns: id;title;owner_role
   :sort_by: id