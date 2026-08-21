# New SINEU family with a U1/U2 snRNA-derived origin in Crocodilia

**Family/row:** SINEU (3 families)
**Source:** Kojima 2015, Genome Biology and Evolution 7(6):1702-1712, DOI 10.1093/gbe/evv100

## Citation
Kojima, M. (2015). A new class of SINE with snRNA gene-derived heads. GBE 7(6):1702-1712.

## Summary
Describes SINEU-1, -2, and -3, three SINE families found in alligators, crocodiles, and gharials (Crocodilia) whose 5' head is derived from a U1 or U2 small nuclear RNA gene - a genuinely novel origin type, distinct from the usual tRNA/7SL/5S rRNA origins seen in nearly all other known SINEs. Only the second "unusual origin" case found in this whole tracker (after SINE28's 28S rDNA origin).

## Sequence recovery
Europe PMC's supplementary-files endpoint initially reported **zero** supplementary files for this paper - a false negative, not a genuine absence (that endpoint simply doesn't mirror this journal's, GBE/Oxford Academic, supplementary material at all). The user supplied the real file directly: `evv100_Supplementary_Data.zip`, a 29-page `SFigs.pdf`.

Text-extracted all 29 pages (PyMuPDF, not just figure captions). Pages 5-28 turned out to contain dense, real RepeatMasker-style alignment output - scaffold names, positions, matched-repeat names, divergence statistics - for individual SINEU copies. The scaffold names (e.g. `scaffold-13046`) are internal to the *Green et al. 2014* crocodilian genome consortium assembly and don't resolve against the species' *current* NCBI/RefSeq assembly (renamed after reprocessing) - but they match **exactly** against the *original 2013/2014 GenBank submission* (`GCA_000768395.1`) before any renaming, confirmed directly against that assembly's own `assembly_report.txt`.

Built a scaffold-name-to-accession map from that original report and fetched all 181 SINEU-tagged hits (130 unique after deduplication) via NCBI `efetch`.

**A real bug caught before finalizing:** RepeatMasker's convention lists descending coordinates (e.g. `174708-174265`) for minus-strand hits. Direct testing showed NCBI's `efetch` does **not** auto-reverse-complement for that - it silently returns the identical forward-strand sequence regardless of coordinate order. 98 of 181 hits (54%) were initially the wrong strand. Fixed by detecting descending coordinates and reverse-complementing locally; verified the fix by confirming same-subfamily sequences share the same conserved internal motifs (e.g. `CCTGGCAGG...`, `GGAACTTGACT...TTGGCCC`) regardless of source strand - they didn't, before the fix.

**Result: 130 real genomic copies** across all 13 SINEU subfamilies (SINEU-1A through 1J, 1G2, SINEU-2, SINEU-3) - the single largest sequence recovery in this whole tracker. See `literature-gap-tracker_sequences/SINEU_130copies_Kojima2015.fasta`.

## Data availability
No dedicated GenBank/DDBJ/ENA accession for a consensus sequence; no Dfam entry. The supplementary alignment data (real, but not itself a sequence deposit) was the actual path to real sequence, via the original assembly's scaffold-naming.
