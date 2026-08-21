# A novel 28S rDNA-derived SINE in mammalian genomes

**Family/row:** SINE28
**Source:** Longo, Brown, Zhang & O'Neill 2015, Genome Biology and Evolution

## Citation
Longo, M.S., Brown, J.D., Zhang, C. & O'Neill, R.J. (2015). GBE.

## Summary
Describes SINE28, a previously unknown SINE derived from the 3' end of 28S rDNA (the large ribosomal subunit RNA) - a genuinely novel progenitor RNA distinct from the usual tRNA/7SL/5S rRNA origins seen in nearly all other SINEs (only the second such "unusual origin" case in this tracker, alongside SINEU's U1/U2-derived head). Notable because it's a gap in the human genome specifically - the best-studied genome in the entire SINEBase bank, showing even "obvious" genomes have missed families.

## Sequence recovery
The paper's own Table 1 gives only 27 human SINE28 locus coordinates - useful but limited to one species. The real find was in **Supplementary Table 4**, which lists 50 SINE28 loci as `<UCSC-genome>_dna_range=<chrom>:<start>-<end>` strings (e.g. `ailMel1_dna_range=GL194859.1:101520-101711`) across 18 different mammalian genome assemblies (human, chimp, mouse, rat, cow, platypus, elephant, and more) - genomic coordinates, not a deposited FASTA, but a precise recipe for retrieving the actual sequence.

All 18 assembly names are registered UCSC genome databases, so fetched all 50 loci via the UCSC REST API (`api.genome.ucsc.edu/getData/sequence`) rather than NCBI, whose accession-based `efetch` doesn't resolve UCSC-style chromosome names like `chr21` for these particular assemblies. 50/50 fetched successfully, verified with a direct one-off test before committing to the full batch.

**Result: 50 sequences** across 18 mammalian assemblies. See `literature-gap-tracker_sequences/SINE28_50loci_Longo2015.fasta`.

**Caveat:** these are raw BLAST-hit-range copies (may include some flanking sequence beyond the exact SINE element boundary), not curated per-species consensus sequences - a real but different kind of win than a clean deposited FASTA.

## Data availability
No GenBank/DDBJ/ENA accession or Dfam entry for a SINE28 consensus specifically; the paper references the pre-existing Repbase "LSU-rRNA_Hsa" 28S rDNA consensus rather than depositing a new SINE28-specific one.
