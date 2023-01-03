#!/usr/bin/python3

##############################################################################################################
# Author: Mathias Verbeke
# Date of creation: 2022/12/23
# Usage: This script translates a DNA sequence (6 frames)
# Input: A DNA sequence
# Output: 6 protein sequences
# Command line argument 1: DNA sequence
##############################################################################################################

import sys

# function that returns a complementary strand (input: DNA sequence)
def get_complementary_strand(dna):
    complementary_strand = ""
    for nucleotide in dna:
        if nucleotide == 'A':
            complementary_strand += 'T'
        elif nucleotide == 'T':
            complementary_strand += 'A'
        elif nucleotide == 'C':
            complementary_strand += 'G'
        elif nucleotide == 'G':
            complementary_strand += 'C'
        else:
            sys.exit("\nError. Invalid nucleotide(s) present in DNA sequence.\n")
    return complementary_strand

def translate_dna(dna):
   
    complement = get_complementary_strand(dna)
    antiparallelComplement = complement[::-1]
    
    protein_sequence = ''
    protein_sequence2 = ''
    protein_sequence3 = ''
    protein_sequence4 = ''
    protein_sequence5 = ''
    protein_sequence6 = ''

    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'!', 'TAG':'!',
        'TGC':'C', 'TGT':'C', 'TGA':'!', 'TGG':'W',
    }
    
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            protein_sequence += codon_table[codon]
    
    for i in range(1, len(dna), 3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            protein_sequence2 += codon_table[codon]
    
    for i in range(2, len(dna), 3):
        codon = dna[i:i+3]
        if len(codon) == 3:
            protein_sequence3 += codon_table[codon]

    for i in range(0, len(antiparallelComplement), 3):
        codon = antiparallelComplement[i:i+3]
        if len(codon) == 3:
            protein_sequence4 += codon_table[codon]
    
    for i in range(1, len(antiparallelComplement), 3):
        codon = antiparallelComplement[i:i+3]
        if len(codon) == 3:
            protein_sequence5 += codon_table[codon]
    
    for i in range(2, len(antiparallelComplement), 3):
        codon = antiparallelComplement[i:i+3]
        if len(codon) == 3:
            protein_sequence6 += codon_table[codon]

    protein_sequences = [protein_sequence, protein_sequence2, protein_sequence3, protein_sequence4, protein_sequence5, protein_sequence6]
    return protein_sequences


if len(sys.argv) != 2:
    sys.exit("\nError: insufficient command line arguments.\n   - Argument 1: DNA sequence\n")

dna = sys.argv[1].upper()
protein_sequences = translate_dna(dna)

counter = 1
for protein in protein_sequences:
    print("Frame {}: {}".format(counter, protein), end = ' ')
    
    if counter >= 4:
        print("\t\t(3' -> 5')")
    
    else:
        print("\t\t(5' -> 3')")

    counter += 1