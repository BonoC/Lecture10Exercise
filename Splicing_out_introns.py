#!/usr/bin/python3

dna_sequence = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
first_exon = dna_sequence[0:63]
second_exon = dna_sequence[91:]
exon_sequence = str(first_exon) + str(second_exon)
print(exon_sequence)

coding_length = len(exon_sequence)
dna_length = len(dna_sequence)
Exon_percentage = (coding_length/dna_length)*100
print("The exon of this dna sequence holds ",Exon_percentage,"% of the entire length.")

