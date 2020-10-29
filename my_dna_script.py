#!/usr/bin/python3

#Question 1:

dna_sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
count_A_nucleotides = dna_sequence.count('A')
count_T_nucleotides = dna_sequence.count('T')
AT_content = (count_A_nucleotides + count_T_nucleotides) / len(dna_sequence)
print(AT_content)
print("AT content is",str(int(100*AT_content)),"percent")


