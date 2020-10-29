#!/usr/bin/python3

dna_sequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
complementary_sequence_1 = dna_sequence.replace("A","t")
complementary_sequence_2 = complementary_sequence_1.replace("T","a")
complementary_sequence_3 = complementary_sequence_2.replace("G","c")
complementary_sequence_4 = complementary_sequence_3.replace("C","g")
print("The complementary sequence is " , complementary_sequence_4.upper())




