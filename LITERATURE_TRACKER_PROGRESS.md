# Literature gap tracker (SINEdb integration) progress

## Done
- Externalized inline CITATION_GRAPH_DATA and OLDER_WORKS_DATA from literature-gap-tracker.html into fetch() calls to sibling JSON files (literature-gap-tracker_citation_graph.json, literature-gap-tracker_older_works.json)
- Restructured main table into 4 labeled subsections (Confirmed New-Family Gaps, Existing Family Updated, Resolved Not a Gap, Still Unverified) with section header rows; sort-by-column still works (sorts within sections, re-inserts headers)
- Added "Predicted / Orphaned Entries" section with Dfam subsection (fetches literature-gap-tracker_orphaned_dfam.json, renders 19 uncited entries) and RepBase placeholder (not yet done)
- Linked literature-gap-tracker_dfam_citation_report.txt as downloadable full report

## Current phase
complete - awaiting visual verification

## Notes for the next run
### Visual verification checklist (human, no automated browser test):
1. Open literature-gap-tracker.html via a local static server (e.g. `python -m http.server` then visit http://localhost:8000/literature-gap-tracker.html) - fetch() won't work from file:// protocol
2. Confirm the citation graph renders (nodes/edges visible, pan/zoom/rotate work)
3. Confirm all 4 main table sections are visible with header rows: "Confirmed New-Family Gaps" (17 rows), "Existing Family, Updated or New Taxa" (10 rows), "Resolved, Not a Gap" (2 rows), "Still Unverified" (2 rows)
4. Confirm clicking any table column header sorts correctly (rows reorder within their sections, section headers stay in place)
5. Confirm the "Predicted / Orphaned Entries" section appears below the main table with the Dfam subsection (19 entries loaded from JSON) and the RepBase placeholder paragraph
6. Confirm the link to literature-gap-tracker_dfam_citation_report.txt works
7. Check browser console for any errors (especially fetch failures for the 3 JSON files)
