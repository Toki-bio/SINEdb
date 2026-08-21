# Task: restructure literature-gap-tracker.html into labeled subsections + externalize embedded data

## Context
`literature-gap-tracker.html` already exists in this repo (a pre-seeded working
copy of a SINE literature gap tracker built and verified elsewhere - it
renders correctly, has a working interactive citation graph with pan/zoom/
rotate, a sortable table, and no console errors). This repo (SINEdb, a
GitHub Pages site) already has several other standalone HTML pages at the
root (`index.html`, `unified.html`, `squamata.html`, etc.), each paired with
a sibling `*_data.json` file that the page `fetch()`s at load time rather
than embedding data inline - **this is the established convention in this
repo and this task should follow it**, not the inline-embedding approach
`literature-gap-tracker.html` currently uses (that approach was a workaround
for a different hosting environment's restrictions, which don't apply here).

Four small data files are already provided as siblings - read and use them,
do not modify them:
- `literature-gap-tracker_citation_graph.json` - the citation-graph node/edge
  data (currently embedded inline in the HTML as `CITATION_GRAPH_DATA`)
- `literature-gap-tracker_older_works.json` - the "older works" graph layer
  data (currently embedded inline as `OLDER_WORKS_DATA`)
- `literature-gap-tracker_orphaned_dfam.json` - 19 Dfam SINE entries with
  genuinely zero attached citation (raw automated pipeline deposits, not
  yet linked to any paper) - NOT currently used anywhere in the HTML, needs
  a new section built for it (see Requirement 3 below)
- `literature-gap-tracker_dfam_citation_report.txt` - a full text report
  (241 species checked) - just needs to be linked as a downloadable/viewable
  resource, not parsed/rendered structurally

## Requirement 1: externalize the two embedded JSON blocks

Find `var CITATION_GRAPH_DATA = { ... };` and `var OLDER_WORKS_DATA = { ... };`
in the HTML's `<script>` block. Replace both hardcoded blocks with a fetch
at page load:

```js
Promise.all([
  fetch('literature-gap-tracker_citation_graph.json').then(r => r.json()),
  fetch('literature-gap-tracker_older_works.json').then(r => r.json())
]).then(([graphData, olderWorksData]) => {
  // ... existing initialization code that currently runs immediately,
  // now runs here once both are loaded
});
```
The rest of the graph code (force simulation, render, event handlers) should
work unchanged once `CITATION_GRAPH_DATA`/`OLDER_WORKS_DATA` are populated
from the fetched JSON instead of a hardcoded literal - just make sure
anything that currently runs at parse-time (before the data existed) now
runs inside the `.then()` callback instead.

## Requirement 2: restructure the page into clearly labeled subsections

Currently the table has one flat list of rows with a status pill per row.
Add visible section headers (reuse the page's existing `<h2>`-style used for
"Citation Graph") splitting the table into, in this order:
1. "Confirmed New-Family Gaps" (rows with the danger/red pill)
2. "Existing Family, Updated or New Taxa" (warn/orange pill rows)
3. "Resolved, Not a Gap" (ok/green pill rows)
4. "Still Unverified" (muted/gray pill rows)

Keep it as ONE underlying `<table>` (so the existing sort-by-column-header
JS keeps working across all rows), just insert a full-width header row
(`<tr><th colspan="6">Section Name</th></tr>` or similar) before each group
in the tbody, and make sure the existing click-sort logic still works
correctly with these header rows mixed in (it should either skip them when
sorting, or the simplest fix: keep sorting exactly as it works today and
only visually reorder-and-label on initial page load, re-inserting the
section headers after any sort too - your call on which is simpler, but
test both fresh-load display AND clicking a column header afterward before
considering this done).

## Requirement 3: add "Predicted / Orphaned Entries" section (new)

Add a new section, clearly separated from the citation-tracked table above
(different heading style is fine, e.g. reuse the `.graph-section` box style
already in the CSS), titled "Predicted / Orphaned Entries — Awaiting Direct
Verification". Explain in 2-3 sentences (for a reader who hasn't seen this
project before) that these are NOT literature-confirmed gaps like the table
above - they're raw entries from public repeat databases with no discovery
paper behind them at all, included here so they aren't lost, pending manual
verification directly against real genome assemblies.

Inside this section, two subsections:
- **"Dfam"**: render the 19 entries from `literature-gap-tracker_orphaned_dfam.json`
  as a compact list or small table (taxon name, record count, family names) -
  simpler than the main table above, no status pills needed since these are
  explicitly unverified by definition. Link to
  `literature-gap-tracker_dfam_citation_report.txt` as "full citation-check
  report (241 species)" for anyone who wants the complete underlying data.
- **"RepBase"**: a short placeholder paragraph stating this cross-reference
  has NOT been done yet (RepBase requires registration/is not freely
  queryable via API the way Dfam is) - do not fabricate any RepBase entries
  or pretend this was checked. Just state plainly this is a planned future
  addition.

## Requirement 4: minimal nav link back to the main site

Add one small link near the top of the page (below the `<h1>`, above the
summary stats) back to `index.html`, e.g. "&larr; Back to SINE-KB". Do not
add anything else that touches navigation elsewhere in the page.

## Ground rules - important, read carefully
- Do NOT modify any of the four `literature-gap-tracker_*.json`/`.txt` sibling
  files - they are already-verified data, read-only for this task.
- Do NOT touch, rename, or delete ANY other file in this repository -
  `index.html`, `unified.html`, `squamata.html`, `data.json`,
  `unified_data.json`, anything under `alignments/`, `plots/`,
  `sub_subfamilies/`, `viz/`, `MSA-viewer/`, etc. This task's ONLY allowed
  edit target is `literature-gap-tracker.html` itself. If you believe a
  change elsewhere is needed, stop and describe it in the progress file
  instead of making it.
- Commit incrementally: externalize the data fetch and commit, then add the
  subsection headers and commit, then add the orphaned-entries section and
  commit, then the nav link and commit - not one giant final commit.
- Verify your own JS changes are syntactically sound before committing
  (`node -c` won't work on an HTML file, but do a careful manual read-through
  of every brace/paren you touch, especially around the fetch/.then()
  refactor, since a mismatched brace there would break the entire page).
- When done, describe in your progress file exactly what to check (open the
  page locally via a simple static server, confirm the graph renders, confirm
  all 4 main sections + the 2 orphaned subsections are visible, confirm
  clicking a table column header still sorts correctly) - there is no
  automated browser check for this task, a human will verify visually.
