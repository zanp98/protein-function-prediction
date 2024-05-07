import numpy as np
import pandas as pd


def read_fasta(file_path):
    fasta_dict = {}
    current_id = ""
    current_seq = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_id:
                    fasta_dict[current_id] = {'sequence': ''.join(current_seq)}  # Ensure dictionary is properly formed
                header_parts = line.split('|')
                if len(header_parts) > 1:
                    current_id = header_parts[1]
                else:
                    current_id = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
        if current_id:
            fasta_dict[current_id] = {'sequence': ''.join(current_seq)}  # Ditto here
    return fasta_dict


def integrate_data(fasta_path, taxonomy_path, terms_path):
    proteins = read_fasta(fasta_path)  # Read FASTA into dictionary

    taxonomy_df = pd.read_csv(taxonomy_path, sep='\t', header=None, names=['uniprot_id', 'taxon_id'])
    for _, row in taxonomy_df.iterrows():
        if row['uniprot_id'] in proteins:
            proteins[row['uniprot_id']]['taxon_id'] = row['taxon_id']  # Ensure this is assigning to a dict entry

    terms_df = pd.read_csv(terms_path, sep='\t', header=None, names=['uniprot_id', 'GO_term', 'subontology'])
    for _, row in terms_df.iterrows():
        if row['uniprot_id'] in proteins:
            if 'GO' not in proteins[row['uniprot_id']]:
                proteins[row['uniprot_id']]['GO'] = {'BPO': [], 'CCO': [], 'MFO': []}
            proteins[row['uniprot_id']]['GO'][row['subontology']].append(row['GO_term'])

    return proteins
