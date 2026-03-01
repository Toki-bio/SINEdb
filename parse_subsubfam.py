#!/usr/bin/env python3
"""Parse sub-subfamily consensus FASTA into JSON for subfamily_detail.html."""

import json, re, sys, os

TAXON_MAP = {
    'Ltr': 'Lichanura_trivirgata',
    'Vla': 'Vipera_latastei',
    'Agr': 'Acrochordus_granulatus',
    'Ael': 'Arizona_elegans',
    'Aru': 'Achalinus_rufescens',
    'Nna': 'Naja_naja',
    'Hpl': 'Hypsiscopus_plumbea',
    'Afe': 'Azemiops_feae',
    'Mta': 'Myanophis_thanlyinensis',
    'Cho': 'Crotalus_horridus',
    'Xun': 'Xenopeltis_unicolor',
    'Cru': 'Cylindrophis_ruffus',
    'Rsa': 'Rhinophis_saffragamus',
    'Cas': 'Candoia_aspera',
    'Bco': 'Boa_constrictor',
    'Cca': 'Corallus_caninus',
    'Asc': 'Anilius_scytale',
    'Eja': 'Eryx_jayakari',
    'Eta': 'Eryx_tataricus',
    'Mre': 'Malayopython_reticulatus',
    'Mca': 'Morelia_carinata',
}

def parse_fasta(filepath):
    entries = []
    header = None
    seq_lines = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if header is not None:
                    entries.append((header, ''.join(seq_lines)))
                header = line[1:]
                seq_lines = []
            else:
                seq_lines.append(line.upper())
    if header is not None:
        entries.append((header, ''.join(seq_lines)))
    return entries

def parse_entry(header, seq):
    parts = header.split()
    entry_id = parts[0]

    # Extract taxon from prefix (before first _ or __)
    prefix = entry_id.split('_')[0]
    taxon = TAXON_MAP.get(prefix, None)
    if taxon is None:
        # try first 3 chars
        taxon = TAXON_MAP.get(entry_id[:3], 'Unknown')

    # Extract copy count from _Nseqs or _aNseqs pattern
    m = re.search(r'_a?(\d+)seqs', entry_id)
    copy_count = int(m.group(1)) if m else 1

    # Notes: everything after the ID, removing the known species name
    rest = header[len(entry_id):].strip()
    # Remove species name variants from notes
    taxon_words = taxon.replace('_', ' ')
    rest = rest.replace(taxon_words, '').strip()
    # Clean up extra separators
    rest = re.sub(r'\s*-\s*$', '', rest)
    rest = re.sub(r'^\s*-\s*', '', rest)
    rest = rest.strip()

    return {
        'id': entry_id,
        'taxon': taxon,
        'copy_count': copy_count,
        'seq': seq,
        'header': header,
        'notes': rest,
        'group_id': None
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: parse_subsubfam.py <fasta_file> [parent_subfamily]")
        sys.exit(1)

    fasta_path = sys.argv[1]
    parent = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(os.path.basename(fasta_path))[0]
    parent = parent.replace('_consensi', '')

    raw = parse_fasta(fasta_path)
    entries = [parse_entry(h, s) for h, s in raw]

    # Determine taxa order by first appearance
    seen = []
    for e in entries:
        if e['taxon'] not in seen:
            seen.append(e['taxon'])

    data = {
        'parent': parent,
        'description': f'{parent} sub-subfamily analysis',
        'taxa_order': seen,
        'groups': [],
        'entries': entries
    }

    out_dir = os.path.join(os.path.dirname(fasta_path), 'sub_subfamilies')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f'{parent}.json')
    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Parsed {len(entries)} entries across {len(seen)} taxa")
    print(f"Output: {out_path}")
    for t in seen:
        count = sum(1 for e in entries if e['taxon'] == t)
        print(f"  {t}: {count} sequences")

if __name__ == '__main__':
    main()
