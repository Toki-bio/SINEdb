# Gathered SINE sequences from the literature-gap tracker

Actual FASTA sequences retrieved for rows in [`literature-gap-tracker.html`](../literature-gap-tracker.html), gathered 2026-08-21. No sequence here was fabricated or estimated — every one traces to a specific accession, Dfam family ID, or a specific supplementary file. For each file below, the **exact extraction method** is documented so the provenance is reproducible, not just cited. Where a sequence required reconstruction (e.g. concatenating alignment fragments) rather than a single clean pull, that is stated explicitly, not glossed over.

---

### `AfuSINE2-3_13seqs_Kanhayuwa2016.fasta` — 13 sequences
**Citation:** Kanhayuwa & Coutts 2016, PLoS ONE 11(10):e0163215
**Extraction method:** **This one was a real error in my own earlier verification, caught by the user.** Both this session's `research-agent.js` pass and the direct supplementary-file check (S13, PCR primers only) concluded AfuSINE2 was figure-only - because both only checked the paper's *supplementary materials*, never its own main-text tables. The user pasted the actual content of the paper's Table 1 ("List of 5 putative 5S rRNA-related SINE sequences (AfuSINE3) and 8 putative tRNA-related SINE sequences (AfuSINE2)"), which contains the full-length consensus sequence for all 13 elements directly, printed as plain text in the main paper. Verified independently before trusting the pasted text: fetched the paper's own full-text XML via Europe PMC and confirmed the exact same table content byte-for-byte. Extracted all 13 sequences (140-494 bp: 5 AfuSINE3 5S-rRNA-derived, 8 AfuSINE2 tRNA-derived) directly from the XML. **Lesson:** checking a paper's supplementary-files bundle is not equivalent to checking its own main-text tables - both need to be checked before calling something figure-only.

### `SINE28_50loci_Longo2015.fasta` — 50 sequences
**Citation:** Longo, Brown, Zhang & O'Neill 2015, GBE
**Extraction method:** Europe PMC supplementary bundle for PMC4994717 included `supp_evv015_LongoSuppTable4.xlsx`, whose sheet B lists 50 SINE28 loci as `<UCSC-genome>_dna_range=<chrom>:<start>-<end>` strings (e.g. `ailMel1_dna_range=GL194859.1:101520-101711`) across 18 different mammalian genome assemblies (human, chimp, mouse, rat, cow, platypus, elephant, etc.) - genomic coordinates, not a deposited FASTA, but a precise recipe for retrieving the actual sequence. All 18 assembly names are registered UCSC genome databases, so fetched all 50 loci via the UCSC REST API (`api.genome.ucsc.edu/getData/sequence`) rather than NCBI (whose accession-based efetch doesn't resolve UCSC chromosome names like `chr21` for these assemblies). 50/50 fetched successfully, verified with a direct one-off `curl` before committing to the full batch. **Caveat:** these are raw BLAST-hit-range copies (may include some flanking sequence beyond the exact SINE element boundary), not curated per-species consensus sequences.

### `MESC_Lsa_rawcopies_Matetovici2016.fasta` — 8 sequences
**Citation:** Matetovici et al. 2016, GBE 8(1):253
**Extraction method:** Table S1 (already known to exist, previously checked only for its citation info) lists 8 Lsa_1/2/3/4/5/8/Nin_1/Nin_2 SINE copies as GenBank BAC accession + position range (e.g. `Lsa_1, CR974470, 55489-55225` - note the reversed coordinates indicating minus strand). Fetched all 8 via NCBI `efetch` with `seq_start`/`seq_stop`/`strand=2` as needed. Verified Lsa_1's stated TSD (`ACACTGACTTTG`) appears at both the start and end of the fetched sequence, as expected for a genuine TSD-flanked element - not just assumed correct. Table S2 (the "provisional consensus sequences" metadata table) was also checked directly and confirmed to contain only descriptive metadata (source database, copy count, consensus length) with no actual sequence column - the MESC/Snail/Vhc/CORE consensus sequences themselves remain figure-only, this row only recovers the Lsa raw discovery copies.

### `SINE1-1_EBu_20copies_hagfish2020.fasta` — 20 sequences
**Citation:** hagfish SINE1-1_EBu study, PMC7245038
**Extraction method:** Additional file 1 (previously assumed to be pure image content) turned out to contain a full multi-copy alignment as extractable plain text via `pdftotext -layout` - not just a rendered figure. Extracted all 20 individual genomic copies of SINE1-1_EBu from the "(A) SINE1-1_EBu" alignment block, stripping the `//` internal-gap markers and `-` alignment-gap characters. These are individual raw copies with their own flanking sequence (not a single averaged consensus), directly reflecting real genomic instances.

### `Leech_SINEs_22seqs_Muller2025.fasta` — 22 sequences
**Citation:** Müller 2025, DNA (MDPI) 5(2):30
**Extraction method:** MDPI blocks all automated access with a Cloudflare-style 403 (confirmed via headless Chrome), same wall as Wiley. User downloaded both the article PDF (`dna-05-00030-v2.pdf`) and its supplementary zip (`dna-05-00030-s001.zip`, 17 supplementary figure PDFs) directly. Ran `pdftotext -layout` on Figures S3–S8, which - unlike most figure-only alignments seen elsewhere in this project - contain clean, unwrapped consensus sequences as plain extractable text before their alignment-block sections, one block per species: HvSINE1-4 (Hirudo verbana), Hman_SINE1-6 (Hirudinaria manillensis), Wpig_SINE1-4 (Whitmania pigra), Hsan_SINE1-4 (Haemopis sanguisuga), Hnip_SINE1-3 (Hirudo nipponia), and HmSINE_V2 (H. manillensis, Fig. S8). A parsing bug was caught and fixed mid-extraction: a stray blank line inside two sequences (HvSINE2, HvSINE3) caused an early cutoff; fixed by only ending a sequence block on a new name-header or the alignment-block marker, not on blank lines. All 4 HvSINE lengths were cross-checked against the coordinate numbers printed at the end of each row in the figure's own alignment block (199/198/195/242 bp) and matched exactly.

### `AngioSINE_24families_Seibt2019.fasta` (degapped) + `AngioSINE_24families_aligned_Seibt2019.fasta` (original alignment) — 24 sequences each
**Citation:** Seibt, Schmidt & Heitkam 2019, The Plant Journal 101(3):681–699
**Extraction method:** This paper's own Data Statement names a real deposit ("Data S1 lists the 24 Angio-SINE consensus sequences in fasta format"), but Wiley's site returns a Cloudflare bot-challenge (403) to all automated access, including headless Chrome - the same wall hit on Leech SINEs/MDPI. User downloaded `tpj14567-sup-0003-datas1.zip` directly via their own institutional access (Uzbekistan Hinari/Research4Life, visible in the PDF's own download footer) and supplied it directly. Unzipped to `tpj14567-sup-0003-DataS1.fas` - confirmed exactly 24 records (SolS-II, EriS-I/II/III, AmaS-XXII, RanuS-I, SaliS-IV/V, and 17 more), matching the paper's own family count exactly. The deposited file is an **alignment** (contains gap characters) - kept as-is in the `_aligned` file, and a degapped ungapped-sequence version was also produced (the plain `AngioSINE_24families_Seibt2019.fasta`) for direct use as consensus sequences.

### `PxSE1-5_plus_related_Han2021.fasta` — 224 sequences
**Citation:** Han et al. 2021, BMC Genomics 22:230
**Extraction method:** Paper's text gives explicit GenBank accession ranges (PxSE1: MW068006–MW068073; PxSE2/PxSE3: MW068074–MW068156; PxSE4/PxSE5: MW068157–MW068229). Built the full ID list programmatically, fetched all 224 in one batch call via NCBI `efetch` (`db=nucleotide&rettype=fasta`). These are **raw individual element copies**, not a single deposited consensus per family — the paper's own consensus sequences are shown only as alignments in its figures.

### `bivalve_21species_dfam_consensus.fasta` — 57 sequences
**Citation:** Peona, Martelossi et al. 2024 (Dfam deposit; the linked paper itself is a tardigrade TE-curation teaching paper, not a bivalve-specific publication — the bivalve families were deposited by the same crowd-curation event)
**Extraction method:** Queried Dfam's API for all SINE families under clade Bivalvia (`/api/families?clade=Bivalvia&clade_relatives=descendants&type=SINE`, 57 results). Fetched each family's actual consensus FASTA individually via `/api/families/{accession}/sequence?format=fasta`. One transient fetch failure was retried and succeeded (verified with a direct follow-up `curl`, not assumed).

### `Sbg1-9_Firsov2022.fasta` — 9 sequences
**Citation:** Firsov, Kosherova & Mukha 2022, PLoS ONE 17(6):e0266699
**Extraction method:** Downloaded the paper's Supporting Information bundle from Europe PMC (`/PMC.../supplementaryFiles`), ran `pdftotext -layout` on S6 (`pone.0266699.s006.pdf`). That PDF contains explicit `>Consensus_SbgN (Xb)` FASTA-style blocks per subfamily (not just a raw alignment) — extracted each block, stripped the whitespace `pdftotext` introduced mid-sequence from the PDF's column wrapping, and verified every extracted sequence's length matched the bp count stated in its own header exactly (9/9 matched).

### `ZymTri_family98_Baril2023.fasta` — 1 sequence
**Citation:** Baril & Croll 2023, BMC Res Notes 16:335
**Extraction method:** Paper's Data Availability statement names a Zenodo record (10.5281/zenodo.8379981). Fetched the record via Zenodo's API, downloaded the deposited `ZymTri_2023.manCurTE.v1_0.fasta` (a 331-family full TE library), then filtered for the one record tagged `#SINE` in its header.

### `SINE_rCom_Kong2024.fasta` — 2 sequences
**Citation:** Kong, Zhang & Ma 2024, Front Plant Sci 15:1397215
**Extraction method:** Frontiers' own site blocks automated fetches, so went via Europe PMC's supplementary-files bundle for the PMC ID instead. `DataSheet_1.zip` inside that bundle contains `Curated_Consensus_Sequences.fa` (462 curated TE consensus records total) — filtered for the 2 records whose header starts with `SINE` (`SINE_rCom` and the uncertain-classification `SINE?_rCom`).

### `Coilia_nasus_SINE_Liu2020.fasta` — 1 sequence (208 bp)
**Citation:** Liu, Yang, Tang, Zhang, Royster & Zhang 2020, Mobile DNA 11:2
**Extraction method:** Europe PMC supplementary-files bundle → Additional file 2 (`MOESM2_ESM.pdf`). `pdftotext -layout` on that PDF shows a table literally titled "Additional Table 2 The consensus sequence of SINE family from genome of C. nasus" with the sequence given directly under a "Sequence (5'→3')" header — parsed the wrapped lines back into one contiguous sequence.

### `PittSINE_Suh2017.fasta` — 1 sequence
**Citation:** Suh, Bachg et al. 2017, Mobile DNA 8:6
**Extraction method:** Europe PMC supplementary-files bundle → Additional file 2 (`MOESM2_ESM.txt`, only 155 bytes). Already a clean, complete FASTA record (`>PittSINE`) with no parsing needed — copied as-is.

### `TguSINE1_reference_Dfam.fasta` — 1 sequence (reference only, not a tracker gap)
**Citation:** Dfam family DF000006319
**Extraction method:** Direct Dfam API fetch (`/api/families/DF000006319/sequence?format=fasta`). This is the pre-existing zebra finch SINE the passerine paper above uses as its comparison point — included for context, not itself a new finding.

### `RUDI_raw_clones_Luchetti2016.fasta` — 3 sequences
**Citation:** Luchetti, Šatović, Mantovani & Plohl 2016, Mol Genet Genomics 291(3):1419–29
**Extraction method:** User supplied the actual PDF directly (paywalled paper, not otherwise accessible). Ran `pdftotext -layout`, then a GLM task (`glm.js`, narrow 3-question scope) read the extracted text and located 3 real GenBank accessions (KT809347 clone D12, KT809348 clone D25, KT809349 clone P14F) plus confirmation that the paper's 25 species-specific consensus sequences (Table 1) were **never** individually deposited under their own accession — GLM's claims were spot-checked directly against the raw `pdftotext` output before being trusted (exact line-quotes matched). Fetched the 3 real accessions via NCBI `efetch`.

### `Squam3A-B-C_Vassetzky2021.fasta` — 3 sequences
**Citation:** Vassetzky, Kosushkin, Korchagin & Ryskov 2021, Mobile DNA 12:10
**Extraction method:** Main-text Figure 1 shows Squam3A/B/C only as a colored multi-way alignment image — not usable for clean extraction. Per standing rule ("always check supplementary before resorting to image transcription"), checked Europe PMC's supplementary bundle first: Additional file 2 (`MOESM2_ESM.docx`) turned out to contain the same alignment as **plain, monospaced text** (parsed via `python-docx`, no OCR needed). The alignment is split into two column-blocks (tRNA+CORE region, then L2-derived+tail region); extracted each subfamily's row from both blocks, concatenated in column order, and stripped alignment gap characters (`-`) to get the ungapped sequence. Presence of IUPAC ambiguity codes (K/M/R/Y/W) in the result confirms these are genuine multi-copy consensus sequences, not single raw copies. **This required reconstruction (concatenating two blocks + degapping), not a single copy-paste** — flagged as such rather than presented identically to a clean single-source pull. Not manually transcribed from any image.

---

## Not yet gathered
- **MetaSINEs** (Nishihara et al. 2016) — confirmed genuinely inaccessible: deposited in Repbase only (subscription-gated), absent from Dfam.
- **Urop** (Kosushkin et al. 2026) — checked Additional File 2 directly (a .docx, hoping for a Squam3-style text escape hatch): confirmed it's only image-license credits, not sequence data. Consensus sequences remain figure-only (Figs. 2/3 of the main PDF).
- **SINEU** (Kojima 2015) — the earlier "zero supplementary files exist" claim was wrong (Europe PMC's endpoint doesn't mirror GBE/Oxford Academic's supplementary files at all, caught by the user, not by re-checking Europe PMC). User supplied the real file directly (`evv100_Supplementary_Data.zip`, a 29-page `SFigs.pdf`): checked every page's text (PyMuPDF, not just figure captions) - pages 5-28 contain real RepeatMasker-style alignment output (scaffold IDs, positions, divergence %) for individual SINEU copies, but zero long ACGT sequence runs anywhere. The scaffold IDs are internal to the Green et al. 2014 crocodilian genome consortium assembly and don't resolve to a public GenBank accession the way SINE28's/MESC's did, so the actual consensus sequences remain genuinely unfetchable - but the file itself is real and was wrongly reported absent.
- **ZenoSINE1 + metulj families** (Ray, Grimshaw et al. 2019) — checked the full 6.7MB supplementary data zip directly (17 figures + 4 spreadsheets): every spreadsheet contains only genome-content proportions/community-membership data, no sequence columns; the one figure that might have had tail alignments (Fig. S7) is a pure image with zero extractable text. Confirmed no sequence deposit exists anywhere in this paper's materials.
- The 4 rows marked `NOT_AVAILABLE` still unresolved (Solanaceae, Amaranthaceae, 18 Branchiostoma SINEs, Nematode/Heligmosomoides) — no accessible full text or deposit found as of this pass.

See the tracker's own "Consensus availability" notes per row for the full verification detail behind each verdict.
