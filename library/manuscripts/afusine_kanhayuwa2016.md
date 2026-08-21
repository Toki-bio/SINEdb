# Short Interspersed Nuclear Element (SINE) Sequences in the Genome of the Human Pathogenic Fungus Aspergillus fumigatus Af293

**Family/row:** AfuSINE2/AfuSINE3 (×13)
**Source:** Kanhayuwa & Coutts 2016, PLoS ONE 11(10):e0163215

## Citation
Kanhayuwa, L. & Coutts, R.H.A. (2016). PLoS ONE 11(10):e0163215.

## Summary
Describes 13 SINE families in *Aspergillus fumigatus*, a human pathogenic fungus - the first fungal SINEs found in this whole tracker (a second, Zymoseptoria tritici, was found later via Dfam). Two origin types: 8 tRNA-derived families (AfuSINE2) and 5 5S-rRNA-derived families (AfuSINE3).

## Sequence recovery
This one involved a real error, caught by the user, in how this row was verified. Two separate checks - an automated `research-agent.js` pass and a direct fetch of the paper's Supporting Information S13 (a PDF, which turned out to contain only short PCR validation primers, 18-22 bp) - both concluded the consensus sequences were figure-only. Both checks were looking in the same wrong place: the paper's *supplementary materials*. Neither ever checked the *main text's own tables*.

The user pasted the actual content of the paper's **Table 1** ("List of 5 putative 5S rRNA-related SINE sequences (AfuSINE3) and 8 putative tRNA-related SINE sequences (AfuSINE2)"), which contains the full-length consensus sequence for all 13 elements directly, printed as plain text in the body of the paper itself. Verified independently before trusting the pasted text: fetched the paper's own full-text XML via Europe PMC and confirmed the exact same table content, byte-for-byte.

**Result: all 13 sequences** (140-494 bp) extracted directly from the XML. See `literature-gap-tracker_sequences/AfuSINE2-3_13seqs_Kanhayuwa2016.fasta`.

**Lesson generalized to the rest of this project:** checking a paper's supplementary-files bundle is not equivalent to checking its own main-text tables - both need to be checked before calling something figure-only. Applied retroactively to re-check other "figure-only" rows.

## Data availability
No GenBank/DDBJ/ENA accession or Dfam entry for any of the 13 families - the sequences exist only as printed text in the paper's own Table 1, never deposited to a database.
