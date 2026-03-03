Lifecycle Checks
================

This section defines simple, automated completeness checks for the SIL 2 Emergency Stop thread.
The goal is to detect missing lifecycle links early (e.g., requirements without verification).


Check 1: Every FSR must be verified
-----------------------------------

Expected rule:
Each Functional Safety Requirement (FSR) shall have at least one incoming ``verifies`` link
from a verification activity.

.. needtable::
   :types: fsr
   :filter: "'verifies' not in incoming or len(incoming['verifies']) == 0"
   :columns: id;title;sil_level;owner_role
   :sort_by: id

If this table is non-empty, verification coverage is incomplete.


Check 2: Every verification must have evidence
----------------------------------------------

Expected rule:
Each verification activity shall have at least one incoming ``evidences`` link
from an evidence artifact.

.. needtable::
   :types: verif
   :filter: "'evidences' not in incoming or len(incoming['evidences']) == 0"
   :columns: id;title;owner_role
   :sort_by: id

If this table is non-empty, evidence coverage is incomplete.


Check 3: Every risk item must have a SIL allocation
---------------------------------------------------

Expected rule:
Each risk assessment entry shall have at least one incoming ``allocates`` link
from a SIL allocation artifact.

.. needtable::
   :types: risk
   :filter: "'allocates' not in incoming or len(incoming['allocates']) == 0"
   :columns: id;title;owner_role
   :sort_by: id

If this table is non-empty, SIL allocation coverage is incomplete.


Check 4: Every hazard must be addressed by a risk item
------------------------------------------------------

Expected rule:
Each hazard shall be addressed by at least one risk assessment entry.

.. needtable::
   :types: hazard
   :filter: "'addresses' not in incoming or len(incoming['addresses']) == 0"
   :columns: id;title;owner_role
   :sort_by: id

If this table is non-empty, some hazards are not covered by any risk assessment.
