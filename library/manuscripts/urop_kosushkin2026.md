# A dimeric SINE discovered in shrew mole is structurally similar to primate Alu

**Family/row:** Urop
**Source:** Kosushkin, Vassetzky, Borodulina & Kramerov 2026, BMC Biology 12:10, DOI 10.1186/s12915-026-02550-6

## Citation
Kosushkin, S., Vassetzky, N., Borodulina, O. & Kramerov, D. (2026). BMC Biology 12:10.

## Summary
Describes Urop, an independently-evolved Alu-like dimeric 7SL-derived SINE in the shrew mole *Uropsilus gracilis* (Talpidae) - outside the only other lineages known to carry a dimeric 7SL-derived SINE (primates, rodents, tree shrews, hagfish). Three subfamilies (Urop-a, -b, -c) were identified, each showing the characteristic dimeric structure: an internal ~120 bp unit repeated twice within the consensus.

## Sequence recovery
Unlike every other row in this tracker, this one wasn't recovered from the paper's PDF, its figures, or its supplementary material at all. The actual research data for this exact paper already existed locally, in a project directory with file timestamps from October-November 2025 (including a "resubmission2" folder) - well before this tracker's fetch pass began, and consistent with the paper's own 2024-preprint-to-2026-publication timeline. This is the paper's own original research data, not a third-party extraction.

Each subfamily's alignment file (`Urop_a.fas`, `Urop_b.fas`, `Urop_c.fas`) contains a pre-computed consensus as its first record, plus 100 real genomic copies (scaffold ID, coordinates, and strand given in each header) from the actual *Uropsilus gracilis* genome assembly. Degapped the consensus record from each file for the 3 primary consensus sequences; degapped all 300 raw copies into a second file.

Authenticity was corroborated independently before treating this as reliable: each consensus visibly contains an internal ~120 bp unit repeated twice - exactly the dimeric structure the paper itself describes, confirmed without needing to trust the file's origin alone.

**Result: 303 sequences** - 3 subfamily consensus (247/266/255 bp) + 300 raw genomic copies. See `literature-gap-tracker_sequences/Urop_a-b-c_consensus_Kosushkin2026.fasta` and `Urop_300rawcopies_Kosushkin2026.fasta`.

**Addendum (2026-08-22 re-audit):** The earlier pass checked only Additional File 2 (image licenses, confirmed empty of sequence data) and never checked **Additional File 1** (Figures S1-S5 + Table S1) at all - a real gap, not a dead end that had already been ruled out. Fetched it via Europe PMC's supplementary-files bundle (`12915_2026_2550_MOESM1_ESM.pdf`) and found it genuinely extractable as plain text via `pdftotext -layout`. It contains: Fig. S1 (~96 examples of free Urop-m *monomer* elements - a structurally distinct, non-dimeric form not covered by the a/b/c dimeric consensus/copies above - shown as short TSD-flanking excerpts, not full-length), and Figs. S2-S4 (21 full-length Urop_c/Urop_b copies with their poly-A tails, printed as complete wrapped multi-line sequences with real genomic coordinates). **Result: 117 more sequences.** See `literature-gap-tracker_sequences/Urop_AdditionalFile1_117seqs_Kosushkin2026.fasta`. Fig. S1's entries are explicitly labeled as partial (TSD-region excerpts only, per the figure's own scope) and are marked as such in the FASTA headers to avoid presenting them as full-length elements.

## Data availability
The paper's own Additional File 2 (checked directly) contains only image-license credits, not sequence data - the actual consensus sequences are shown only as alignments in the paper's Figures 2 and 3. No GenBank/DDBJ/ENA accession or Dfam entry exists for Urop. Additional File 1 (see addendum above) does contain real sequence data and was missed on the first pass.
