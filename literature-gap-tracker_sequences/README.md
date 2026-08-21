# Gathered SINE sequences from the literature-gap tracker

Actual FASTA sequences retrieved for rows in [`literature-gap-tracker.html`](../literature-gap-tracker.html), gathered 2026-08-21. Each file's provenance is documented below — no sequence here was fabricated or estimated; every one traces to a specific accession, Dfam family ID, or a specific supplementary file, verified by direct fetch/extraction and (where noted) length-checked against the source's own stated value.

| File | Family/row | N seqs | Source | Citation |
|---|---|---|---|---|
| `PxSE1-5_plus_related_Han2021.fasta` | PxSE1-5 (+18 related) | 224 | GenBank accessions MW068006–MW068229 (raw element copies, not a single deposited consensus per family) | Han et al. 2021, BMC Genomics 22:230 |
| `bivalve_21species_dfam_consensus.fasta` | 21-species bivalve SINE set | 57 | Direct Dfam FASTA fetch, one per family accession (e.g. DF003586478) | Peona, Martelossi et al. 2024 (Dfam deposit; paper itself is the tardigrade-curation paper, not a bivalve-specific publication) |
| `Sbg1-9_Firsov2022.fasta` | Sbg1–Sbg9 | 9 | PLOS ONE Supporting Information S6 (PDF), each `>Consensus_SbgN` block extracted and length-verified against its declared bp | Firsov, Kosherova & Mukha 2022, PLoS ONE 17(6):e0266699 |
| `ZymTri_family98_Baril2023.fasta` | Zymoseptoria tritici SINE | 1 | Zenodo-deposited full TE library (331 families total; this is the only one tagged `#SINE`) | Baril & Croll 2023, BMC Res Notes 16:335 |
| `SINE_rCom_Kong2024.fasta` | Castor bean SINE (SINE_rCom) | 2 | Frontiers Supplementary DataSheet_1.zip → `Curated_Consensus_Sequences.fa` (462 records total; these 2 are the only SINE-tagged ones) | Kong, Zhang & Ma 2024, Front Plant Sci 15:1397215 |
| `Coilia_nasus_SINE_Liu2020.fasta` | Coilia nasus SINE | 1 | BMC Additional file 2 (PDF table, consensus given explicitly) | Liu, Yang, Tang, Zhang, Royster & Zhang 2020, Mobile DNA 11:2 |
| `PittSINE_Suh2017.fasta` | De-novo passerine SINEs | 1 | BMC Additional file 2 (plain-text FASTA, already clean) | Suh, Bachg et al. 2017, Mobile DNA 8:6 |
| `TguSINE1_reference_Dfam.fasta` | (reference only, not a new gap) | 1 | Dfam family DF000006319 — the pre-existing zebra finch SINE used as a comparison point in the passerine paper above, not itself a new finding | Dfam |
| `RUDI_raw_clones_Luchetti2016.fasta` | RUDI | 3 | GenBank KT809347 (clone D12), KT809348 (clone D25), KT809349 (clone P14F) — the original discovery clones. **Not** the 25 species-specific consensus sequences the paper builds (Table 1) — those were never individually deposited under their own accession; see the tracker row's notes for the full breakdown | Luchetti, Šatović, Mantovani & Plohl 2016, Mol Genet Genomics 291(3):1419–29 |

## Not yet gathered
- **MetaSINEs** (Nishihara et al. 2016) — confirmed genuinely inaccessible: deposited in Repbase only (subscription-gated), absent from Dfam.
- **Leech SINEs** (Müller 2025, MDPI) — supplementary material link returns HTTP 403 to automated fetches (including headless Chrome); needs a different retrieval approach.
- The 8 rows marked `FIGURE_TABLE_ONLY` in the tracker (Urop, MESC & Snail, AfuSINE2, SINE1-1_EBu, Squam3, SINEU, SINE28, ZenoSINE1+metulj families) — sequences exist only as figure/schematic alignments in their papers, would need manual transcription from a PDF image rather than a clean extraction.
- The 5 rows marked `NOT_AVAILABLE` (Solanaceae, Angio-SINE, Amaranthaceae, 18 Branchiostoma SINEs, Nematode/Heligmosomoides) — no accessible full text or deposit found as of this pass.

See the tracker's own "Consensus availability" notes per row for the full verification detail behind each verdict.
