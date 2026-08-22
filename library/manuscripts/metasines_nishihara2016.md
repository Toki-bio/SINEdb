# MetaSINEs: Broad Distribution of a Novel SINE Superfamily in Animals

**Family/row:** MetaSINEs
**Source:** Nishihara, Plazzi, Passamonti & Okada 2016, Genome Biology and Evolution 8(3):528–539, DOI 10.1093/gbe/evw029, PMC4824008

## Citation
Nishihara, H., Plazzi, F., Passamonti, M. & Okada, N. (2016). GBE 8(3):528–539.

## Summary
Describes a fifth SINE superfamily (after CORE-SINE, V-SINE, DeuSINE, Ceph-SINE), the **MetaSINEs**, defined by a shared 66-bp "Meta-domain" central sequence. Two distinct findings are bundled in one paper:

1. **13 novel MetaSINE-superfamily members**, one per species, spanning an extraordinary taxonomic range — medaka (OrySINE1), salmon (SalSINE1), hagfish (EptSINE1), lancelet (BflSINE2), cuttlefish (SepiaSINE2), two bivalves (BivaMeta-SINE1, BivaMD-SINE1), two gastropods (LitSINE1, HalSINE1), parchment worm (ChaetoSINE1), brachiopod (LinSINE1), and two cnidarians (ClySINE1, HydSINE1) — plus 2 previously-known sea urchin members (SINE2-1_SP, SINE2-2_SP), for 15 total MetaSINE-superfamily sequences. This breadth (fish to Cnidaria) implies a common origin at least 640 Ma.
2. **8 novel SINE families found specifically in bivalves**, spanning 4 different superfamilies: MetaSINE (BivaMeta-SINE1, BivaMD-SINE1 — same 2 sequences as above), DeuSINE (BivaDeu-SINE1), V-SINE (BivaV-SINE1/2/3), and CORE-SINE (BivaCORE-SINE1/2).

**Cross-reference to this tracker's "MESC & Snail" row**: the paper's own discussion states that Matetovici et al. (2016, published independently around the same time) found essentially the same superfamily under the name "MESC-SINE" — the two papers' bivalve SINEs overlap on 3 identical families (BivaV-SINE1≈, BivaV-SINE2≈, BivaCORE-SINE2≈ the corresponding MESC-superfamily members). The two rows describe overlapping but not identical underlying discoveries.

## Sequence recovery
The main-text figures (Fig. 2: the 13-member cross-phylum MetaSINE alignment; Fig. 4: Deu/V/CORE-domain comparisons) are raster images in both the PDF and the full-text XML (confirmed via direct Europe PMC XML fetch — the `<fig>` nodes contain only captions, no extractable alignment text) — these 13 species-spanning sequences remain **not recoverable as text** from this paper.

The user supplied the actual supplementary data file, `evw029_Supplementary_Data.zip`, containing `SupplementaryMaterial.pdf`. Unlike the main-text figures, this PDF's **Supplementary Fig. S1** ("Sequence alignments of the SINE families in bivalves") turned out to be genuinely extractable plain text via `pdftotext -layout` — a full multi-species, multi-block alignment covering 7 of the paper's 8 bivalve SINE families (panels A–G): BivaMeta-SINE1, BivaMD-SINE1, BivaV-SINE1, BivaV-SINE2, BivaV-SINE3, BivaCORE-SINE1, BivaCORE-SINE2. The 8th family, BivaDeu-SINE1, is explicitly stated in the figure legend to have only one species' consensus (Thracia pubescens) and was not part of this multi-species alignment.

Parsed by concatenating each named sequence's row across all wrapped alignment blocks (in appearance order) and stripping `-` gap characters. **Verified before accepting**: for the two "full" (complete, not truncated) sequences whose alignment coordinates start at 1, the stated end-coordinate in the source text matched the computed degapped length exactly (BivaCORE-SINE1_RuDe: 203 bp both ways; BivaCORE-SINE2_MiYe: 351 bp both ways) — confirming no blocks were dropped or misaligned during concatenation.

**Result: 63 sequences** across 7 bivalve SINE families (multiple species/copies per family — "full" = complete consensus, "partial" = truncated/partial consensus per the source figure's own labeling). See `literature-gap-tracker_sequences/MetaSINEs_63seqs_Nishihara2016.fasta`.

**Not recovered**: the 13-member cross-phylum MetaSINE alignment (Fig. 2) and the Deu/V/CORE-domain comparison (Fig. 4) — both main-text-only, image-only figures. BivaDeu-SINE1's single-species consensus was also not in the extracted figure (not part of the multi-species alignment).

## Data availability
298 individually-sequenced PCR-cloned copies were deposited at DDBJ/EMBL/GenBank under accessions LC122973–LC123270. All SINE **consensus** sequences (the ones in Figs. 2 and 4, and Supplementary Fig. S1) were deposited at Repbase (subscription-gated) — confirmed absent from the free Dfam database. The 63 sequences recovered here come from the supplementary figure's own printed text, not from either database.
