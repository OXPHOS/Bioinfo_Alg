"""
Input: a pattern and a sequence
Ottput: the position where pattern appears in sequence

Note: In file reading part, non alphabetic letters are removed
"""

import urllib2

nucleotide_match = {'A':'T','T':'A','C':'G','G':'C'}

def reverse_complement(seq):
    length = len(seq)
    reverse_seq = ''
    for i in range(length):
        reverse_seq += nucleotide_match[seq[length - i - 1]]
        
    return reverse_seq

#seq = 'TTCCAGGGGCCCACCGCTACCGGACGTAAGTCCTGCCGAGAAGTTTCGTGGTAGTTGTGGCGTGGTCGTGTAGCGCCGGCAGGCGGTATGACTCTAACTCAGACGAATGAGATAGTATAGAACAACGGCACTTTTAATCAAGTGCCCACCTGGCTACGTTCCAGCCGTTATTAGATTGTGGACTCTGTCTTGAGCCAGTAATTTCCCTGTTATACGGAGATATATGATTATATCTACACTAGCCTCAAAGTTTACCCCCAGCGGGTCCTTGATTTGAGTAACTGCTCAGGTGTAATGCGGAGTGTCGTAATTATCATGCCGTCCACCGTCTCTCAATTCATAAAGTCCCAAGGAGCTAAGGCTTCCGTGTGCCTCAGTCCCGTACGCAATTCGTTGTCCGAGGCCGCCGTGCTTCGCTCTCATAGACCAAGACGTAGTCGGGCATTTCAATACTACACATATTGGCGGTCAGTCGACACTTTCGACCTGAGGAGCCGGTAGGCACGATGGACGCAGCCAAAGTCACAGGTTGGAGCTGTTGTAACATCATAGACGAAAATTTGACCGTATCCGTGGGCTGAGATAGGAGGGGGTGGGGGTATATGTTCCAGCTTACCACCCGACATGGCCGCTGGTGATCCCCTGAACCGGCAAGCGGGTCTAGTCTTGCTTACATCATTGGAAATACGAGATCCCCTGCCGTTTACGAGGCCCAAGCTAACTTCCTACCCAGGGCGTCCAATACTACCGGATATGGTAATGATGGAGTCGTGTGCAAACCGAAGTGGCGACCCGTCCGGCAAGCCTCACCTGGATGTTCTCCTCTAATGCGGACCATGCCGGCCTTTTGACGTAAAGCTCCGTAGACGGGGTCCCGACAATCGCCGCAACTATGATTGTACAAGAATTTAATACATAGCGAATTGTTGTCATATGTGATTACTTGCACCGGATGGACGTAATGCCGGACGAGCTTTTAGATTTCTACGAACGCTGGTCACACCGGTACCACGAACTGAATTATCGCGCCCGGAAAGCATATCCCTGCTTGCAGATCTGACTCAACGCGTAATGCATGTCAGGGGTAGCTGCAGATAACTTCTGCCTGTCCATGACATACTCCTATGTGGACCGCGAGCTAAGAGCGATGAAATTCACGACCTATGCATTAATTCATCTGAATGACAAGATTGCGTGATGGTGTTTATAATGTATTGGTATTTACGCATGAACCTACGTTTCCCTTACCCGCCGCCAAGCCAAAGGCGCAGGCAATGGCATTTCATTATTTAGCTAGAATTGTTACCTTGACCTAGATGGTGCTACCCGTATAAGGTTTAGCTGTGGCAGGGGCTTACTTGCGAGCATAGCTAACAAAGATCCGCTTCCTGCCACCTTTTCCCCTTGTAGACCCGCCGCGATTCTAATTATCTCACGACTGCGCAGAATAAGAGTAAGTATAATATTGGAGGTAGCATAATTCGTTAGCCAACGCACTGCTTAGCAGGGTATCCACCCGGTGCGATAGATGACTAAGTCTTGGGGGTCCCTAGTTAATACACCAGCTATGTCTTCCTACCCATCCGTTATTCCACAACTGAAGTCAATAACGCTCTATTGAGATTACACTAGAGTTTCCCACAGGGGTATCGTCGATGTCAGGATACAGTGCAGTTATATAGCAAACATACGGGTACAACGGTAGCCAGGCAAGACGTACTAGTTGGAGTACAAAGCTGAATACAGCATAAAAGGGCTGGGAAGGCAAACCCGTTTTCCCCACTAATTGTGTCTGCCCGGATTGCTCAGGCCAAGAAAGACAAACTCAAAGGGGCTTTCGCAGTCCAGATGCGTTTCCTCCGGGTAGGTGTCATGGTAAGTCACTGGGGAAAACCCAAAACTGCAGGGACTAATCTATTTATGGGAGTCCTCACTTTATTCTGAAGAGCGAACCACACACCGTTGCCTGGCATAGAAAAGGGCCGGCGCTTCCTATGAATCGAAGGACTAATGGTTTTCTATGAAATTGAAAAGAGCATAGACGCAGGAAACCAGTGATCTTGGTATAACCCAAGGTTTAATTTGGGCGATTACTAACGTGAAGCCACCATATAAGCTTGTGGCCCTAGTAACTTCCTGCTACTGATGGGAAAGATTTCCTGCCGGCCTCTCATGGACAACTTCCCACTCAGAGATTCGTCGACGATCCCGGCCTAGAGAGGTTAACATTATAATCGCTATTATACGCACTGTATCGTTTCCTCCTCATTATCTGCATCTTGGCTAGGCATCCCGTGAAATGTGAGCGGGGCACCGACGTACCCCACCCGGCGTGACTATGAGGGTGGAGCCGCAGTGCTGTAGTTAGTGATTAACGTATACGCTATCTGTCTTAGTAGCATCAACAGATCGGTCATGCTCAACTAGCATCACATCACAAACCGAACAGAGTTAACGATAAGATAGATGTTCATCGCTGCTAAGGGGTTATGTCCGCTAGCCACGTCGCCCCCGGGCTTAAACCAGATATGCGCTTTCGGTTATGTTGACAGCAAAAACACTACCCGGTTCTAATACTAAATAAAGGCTCAGTTGCAATGGTCAGTCCTTATTTTTGATCACATGAAGGCCCGCGCGTAACCCAAATGCAAAGAATCCTTGTAGATTAGCGCAGAATTTGATCGCTTAGCTGTGGACGTCAGGAGTAATCGTACGCTACGTACCCCAGCTACGTACGGGACTATACGGTAGTGTCTCATCACTTGTGGTTCGTGATGGATCATTTAAGGGGTCGTTTACAAGGAGACCCCTTGGGTGATGACTCGCAGACCCTTTGCGTCTGGTGGTACTGCAGTCTTTGAAGCGAAACGCGCTGTCCTGTAGCGCGATATATACGTATAGTCGTCAATACCATGGTCGGTTCACCAGCTAAACCGAATCGGGCCCAATAAGCACATTAGCGCGTGAGGGACACTCCAAGTGCACAGTCTTTCCCACATGATCGTGTGCCCCACAAACCTACTTTGCGTCACGAACCCAGATGACTATCCTTACTTCATAGATAGCTACCATTCCAGATCAGCCGGGAGGACTGTTTACCTCGTAGAGCAGAACTAAGTGTGGTAGGGCCAAGCGCACCAGCTCCATAGGAGATTGTGGAAGAAACAGTAGACGCTGGTAGCAGAAGGTACTGTGCGTAATATTGATTGATTGGGGCCCACATTGCAAATCGATAATATGAAGGGTAGAGAGCGTGAAAAGATGTATCCACCAACGAATGACCGATTCAATGTGAATGGGGGGAACGCTGATCTAGGCCTGAGCATGCAAAAAAAGAGCGCACGATTTACACCCTCATCTATGGATCAAGACCCGGACTCGGGCTTTACGCCATGTGGCGATGGATAAGTGGATGTTTAGAGTAGTATGTTGTCTTCGGTCTGAGATAATGGTTACCAAGCCCCGTGTCCGATATACGTGAGTAAATCCGACACTTTTTGGTATCGTATGCTATGTGATTAGCAATGACTGTCGGTTAATCAAGTTAGCCTGATGGGAGGACTATTACCAATGACCGCCTAATAAAACGTGCGGTAACTGCACGAGGGTCCATACGGGCATATCGCATACCTCAGTGCAAACGGGATTATCTCATCTGCTTGGTTGGTACTGCTTGCTTATAGGTAAGCTGCGTTCATAGGCCAGTCAGTAGGGTAAGAACTCGCGTTCTAGTGTACTTTCTAACAATTTCGGTATTACTCGGAGAGAACGGCCATGGTAAAAGCGGCGCAGGTGTTTAAGTGGTAGGCCATGATGTCATGCTGTTGCCGTTATCTAAATAGATGAACTGACTCGGACGCCACCGTCTGTTACAGCTCGTAATCTTTACGCGTGACCGGCCCACCCTACCCGTAGCTATCGTGGCTACCTCCCGCAAGGCTTCATAAGACGGGAAGCATTTGTAAGCACAGCAATAACCGGGAAGATGTTTGCCGAATTTTGCCTTAGAGACTCATTCGGGGTACCCTGCATGGAGGGGAACGGTCAGCCTATTGAGCGTGTGGAATTTAGAGCTTTAGACCCAAAGGCACTGTAGACCACGACGGAGGACCCAGGCCGTGACAATCAGGGGCGGCCGTTTATCGACAGGATTCAGCGTCAATGACAGATTCGACCGTTGGATTATTCGGGTCAGCATATACTGGTGTGGATCAATACTCTCTAAAAACCTATCCAGGCGGTCTATCCTGGTTTCCCACAATGGCAATTCCCCCATTACCGGTCCAAAGCAGTAACACGCGATGCCATCTCAGTCCCAAGTTCCGGTGCCGTCGGCGTATGTCGACCACATTCATGTCTTGGAGAGGGTCGGTAAAACCTCTTTTTCTTTTCTGGGGGTCAACCATCAAGCCGTCGGGTCCTCTTAATACTTGAAGGACTCTGGTATAGAGTCATGTATCCCGGAACGGTACACTCGCCAAATAAGAGTTGCGGCCACATCTCAAGTCAAACCATTTAAGTTAGTACCCATATTTGTAAAATCTCGCAAACCCGTTGGTCTCATGAAGCCAAATACAAGGTTTGGTACAAACTCCGGAAGCCTAGCCCTAAATAAGCGGCAAATGAGGATGGCGCAGAAATCACCGACTGCGAGTTTTTGTACTCGTCTATCAAGTAACAAAGCTTCGTCAGCGACTAAAATGGGGAATGAGCGTAATGGGAAGTTCCGGGAGCGTACGGACCAGCCCAGTTCAACACCTCGGCGAGACCAATTTGCCGATGGCTCAATGGTAACAGACGTTGACTCGAGCTACGCTGCGGCCTGGCAAAGAGAGTCGATCCATCTTATGCAGGGTATGCGGTCCCAGATGATATTCGGAGTCAACAAGGATAGGTTCGACATTACGGGACGGGCCTTGCAGAAGGCCCTTCTTTACACCGTTCCCCTTTTGATCCCTTAAATAGCCCGACATTCAGACACGTCCCATCCCACGCGGGTTGGGGCGAAGCTAGACAGATGATTGCCAGGCGGATCACTAGATATACCCGGAGGGGTCCAATTTTTGGGTATCTCTACCGAGTGACGATCGGCCATAAAAAGTCCATGTCGGGCCGCAGGACCCGGCCCATCGGCGACGCTACCGTCGATCTGTAGAGAGTATAGTAGGAACCTATTGAGCGAAAGAAGTTTGATAGGCCTACATCTCTTAGGTCGAGCAAGTGTTGCCAGGAGGTGTGCACGCATTCACTTTGCTCCCGTTCCGAACTTTGGCCTGTAAGCAAGAATGGTGTATAATATGCGAGTGCGAAAGAGTAGGGTCCCCTAGTACGTTTCCATACCGCTTCATACACAACAGAAGCTCGTTGTTTTGTAACGTGAATTTCGTTTACAAAAACTATTTTACAGTTGAGGGTGTCGCCCATTCTGTGGTTCGTGAATAGGTGTTCTCACGCACCTGGCCTGCTTTTCGACGTTCCTAGTTAGCTATTCCCGACCGCTAATGCTACATCGCGAGGTTGCATGTGATTGCACTAGAAAAGGGATCATGTTAAGTTGTACACGTCGAACAGTATAGGTGTTACTGATGAGAGCTCCGCCGCATTGAGAATCGCACGAAAGTGCTTTGGGCGTAACCAAAACCGCCTCATCGTGCCATGGCGATATAGACGGTCCTCACCTTGGGTTTCACACCTGAGACTTAAGTGCAAGCGTACTCGGCACGTGATCGCCGATTTGACCCCCGGGCTATGGGTGCAAGATCCGGGAGGGAGAAGTGCTCTGCGAGTTAATGCGTCAGATTGCATAGGCTAGGGGGGCGTGATCAATCGGACCTCCATCACTAGCGCTAGTCAACGTCGCGTAAACGCGTTCTCATTGAGTATCGCATGATAGGCCCGGGCACCGGACAACTAGCCGATGTCCTACCTAGAATGGCCCGTTTACTGGTTCACTGAGGTGTCTATTTTTGTTCGGCTGGGGGGCCTAACTTGGGCTTAGATTGCAGTTGTGATTGTCCTAATCAGACTTACCGAAGAGGGGCCCCCGCATTTTGTAAGGGGTGGCACCCGATATCCGAGTCGGCCCTGGCTCTAAGCTCTGGTGATCGTACCGAGTCACCGAGTTATAGCTTACTGTTATACTGGTGAGGCACCCGCAGAAGGCAAGACGATCCGGGTTTCACTGCGGGGCCTCTGGCGGGGAGCTTTATCTCCCCTGCATGGCTATTGTCAGCAGTTACATAGTGAATCTAATAGGTCGTAAATATAGAGGTTGACATAAGTTGCTCTGAACGAAGGGTCGGTCAAGACGGGTGTATAGGGGAAGCAGAAAGACGCAGCGACGTGGAAGGTGATTGCGAAGGTATATGTCAAGGATGGCTTAACGCTGCAGAGCAAAAGCCCTCCAGTGGAGTATTAGCCCGCGTAGACTGAAGCGTGGCATGCGGCTATGGCGCTAGGCGCCCATGGAATTTGCCGTGTACCACGTCTTGCCGTAGGGGACAAACTCCAATTACGGGCTATTAAGATCTGTGCCTAACGCGTGGGCTCATCCTCATTTAGTCCTGATCCAAGTTTGATGTCGGTCGGTATACAGGCCTCACTATGTATCGATGGAGGACGAACTAGACATGAGTAGGAACGAAGTGCTAGACAGGCATCAATCAAAATGTTGGGGGTCCATTACATCAGCTCGAGCATGCTGCGTTACCCCAAATGGTAGGAGCAGATTAGATGTTTTAACTGCTCACGAAAAGGCTGTACGAGTTTCTTGCGCGCTAGGCTTGATAAGATAACGGTACATGTGTGGTCAAAGGACCTCAGGCTGGGCCGATCCGCACTTGCGCGCTTTGGAGTCTTCGAGCAGCCGGGTACTAACGAGGAACCCTTGTGTTGTTTGAAGAGCTCGATTCTCGCTCGAAAATAGATCGAAAAGGGCGGCATGAGATCCGTCGAGGCCTCGTTAGGAAATTAACGCTGCGCTTTGCACCCCCTGAGTCATTAGCTGGGCCGTTCGTGCACTAAACGCCGTTCTGTTGAACAGGAACGAATGGCTGCTTAAGTGGCGACGCCGTCATCGGTCGTTTAGAAGCTTGGAGCTGTCGATAGTAGGACTCTTCGGGACGACCCAGCTCTGCTGACACGGGGTGCTGCTTACCACTTCCGTGGGAAAACATTCGGGACGTTAGAGAATCTAAAGCAAGCTAGGCCCGACCCTGGTGCCTCCCACTAAGATTGTCACGTTACGGTGCATGATTGCGGGCATTTGTGCAGCCCGCTGCGTATCACTTACCGAGTGCGTTACGACGATTAACACTCGTATACCAAGGGAAAGCGACTACCTAACGGACTAACAAGGTAAGTCCTCGTTATATGGTTTAACCAATCAGAATGGACGAAACAAAGAATTTGACCAGAAGTTCTTCTCTGACTGTTATACCGGGTACTGCCTGCGGGTACAAGTCACGCTGGGACTTAACCATCGGCCGTATATGCTGGGGCAGGTCAGATTTAATGTCGCTACGTTTCCTTGATTCTGCGTCTCGTATCAGAGTTTGTAGGCGCGGATGACAGCCCGCCTGACCCAAAAGAGCGTGGAAGACGATTTTGGTGCTGATTATCGTAACACTAACTCGTACACGGCGTTAGATGTATCGGAAACCCTGCGCCAGTGGAGCACTACCAGTTCCCTCAGGAGAGACAGTGGAACCCCTTGCGCCGCTACGCAGGTTGGTTCTTAGATCCAGATGCAGGGCAAGACTCGGAAGTAACAGTTTCTGTCGACCAGACATCCCGTCACTTTCGCGTCAAACACACGCTGAGTCTTTAAGGTGGGGTTGACCTAAGCACATGACGGGGCTCTACACAAAAGTTACCATCTAACTGGTTGCCGAAGCTTACGGTTAGTTCTTAAGCTCCTGGAGTAACCGCTATAATGCCAAGCCAGGATGGAAAACCTCCGACTATGTCGGCCGTTGACCGTTGCCGTCTATGTGGAGTGCCACGGGCCACGATCGGATAAGCGGACCCGTAAAGAATTGCCACAATTAGGGGGGATCGCGCGTTCATTCATAGAACACAAGATTGTGTTGCACAAAACGGGGGTGAGCAATGCACAATTATGGAGACAACAGCGTATGACTGACTGGCACGGTTGTACGCCACGCGCCTCTAACCAACATGGCCATAATAGTCTAGCGACGTTATTAGGCATATTAATAGTGGATCTCATTCCGATTTTCCGACTTCCGGAATAACGCTTATGGGCGTCGCCTTCGTGTGGTATATCGCTCCGAACGAAATAACGGTGGTGAGACGCGCGGGCTGCCCAGAGTGTTAGCGCATGAAAGATGGTGGAAACTATTTCCTGGCGGGCTACTGCATATGTAGTTGGCGCTTTTAAAAGTCGTAACCTATCTAGTT'

#print reverse_complement(seq)
        
def pattern_matching(pattern, genome):
    match = ''
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i+len(pattern)] == pattern :
            match = match + str(i) + ' '
#        if reverse_complement(genome[i:i+len(pattern)]) == pattern:
#            match = match + str(i+len(pattern)-1) + ' '
    return match

URL = 'https://stepic.org/media/attachments/lessons/3/Vibrio_cholerae.txt'

file = urllib2.urlopen(URL)
genome = ''.join(ch for ch in file.read() if ch.isalpha())
#print genome
#genome = 'GGCCACTGGCCGAAGTACTGGCCCTTACTGGCCGGGCCACTGGCCACTGGCCAATCACACAACCGACTGGCCCACTGGCCAACTGGCCTGACTGGCCTACAGTTCACTGGCCACTGGCCACTGGCCACTGGCCTACTGGCCACTGGCCTAACTGGCCGGGTGACTGGCCCACTGGCCCCCACTGGCCCCAACTGGCCCGTCGGTACGCCAAAGGCGTACTGGCCAAAACTGGCCTAAACTGGCCAACTGGCCTACTGGCCCAAGACCACTGGCCAAGTTCTTTACTGGCCCAACTGGCCGTCACCGACTGGCCGAGCGACTGGCCGTACTGGCCTCACTGGCCACTGGCCGAGGCGACTGGCCACTGGCCACTGGCCTTAATAACTGGCCAGGCTACTGGCCATCACTGGCCACACCTGGACAACTGGCCTACTGGCCAACCGTACTGGCCTAAACTGGCCCCTTACTGGCCACTGGCCTCACTGGCCCACAACACTGGCCGGGTACTGGCCACTGGCCGACTGGCCAACTGGCCGGTCCGTCACTGGCCGTCAGCCAACTGGCCACTGGCCCTACTGGCCTAACTGGCCCACTGGCCACACTGGCCACTGGCCACTGGCCGTTTGACTGGCCACTGGCCACTGGCCACTGGCCGTATGCACCGAACTGGCCTACTGGCCACTGGCCCCGACTGGCCACTGGCCGCCTGTCACTGGCCTTACTGGCCACTGGCCGTACTGTGACTGGCCAACTGGCCGATGATAAACTGGCCAACTCACTGGCCACTGGCCACTGGCCTCGACTGGCCGGCCCACTGGCCGCCACTGGCCCGACTGGCCTACTGGCCTACTGGCCAAGACTGGCCCACTGGCCGGGACTGGCCGGACTGGCCCCAACTGGCCACTGGCCTGGCACTGGCCTACTGGCCGTCCGGAGTACTGGCCTGAGACTGGCCGACTGGCCACTGGCCAACTGGCCCCGGACTGGCCTACTGGCCACTGGCCGGAGCATTACTGGCCACTGGCCGACTGGCCACTGGCCACTGGCCGGGCTGTACTGGCCACTGGCCTATCCTACTGGCCGACTGGCCAACTGGCCTCACTGGCCCTCACTGGCCCATTGTTAATTATGTCATACTGGCCTGAGTTTACTGGCCGACCACTGGCCACTGGCCAAAAGACACTGGCCTACCATACTGGCCACTGGCCTTACTGGCCAACCTCTCACTGGCCATTTGGCAGCTACTGGCCGACTGGCCCGTCCGTACTGGCCTTACTGGCCATAACTGGCCAGACTGGCCCCACTGGCCCACTGGCCCTGTAACTGGCCGACTGGCCTACTGGCCCACTGGCCTCACTGGCCAATAGACTGAAAACTGGCCACTGGCCAACTGGCCCTACTGGCCCGCACTACTGGCCGTACTGGCCACTGGCCACTGGCCCTACTGGCCACTGGCCACGGACTGGCCACTGGCCACTGGCCACTGGCCACTGGCCCACTGGCCTAGGAGTTCACTGGCCGACTGGCCAGGCAGCACTGGCCGTGACTGGCCACTGGCCACTGGCCACTGGCCACTGGCCACACTGGCCTACTGGCCACTGGCCCGTTTTCAGCACTGGCCGACTGGCCAAACTGGCCAATAGACTGGCCACTGGCCCAACTGGCCATACTGGCCAATACTGGCCTGCACTGGCCGACTGGCCAACTGGCCATCACTGGCCAGACTGGCCACTGGCCTGGACTGGCCAGATTACTGGCCACTGGCCTCGACTTGTACTGGCCACACTGGCCACTGGCCACTGGCCTACGGTCAACTGGCCACTGGCCACTGGCCCAAGACTGGCCACTGGCCCTCGTGTGACTGGCCGCTTACTGGCCCACCCCACTGGCCAAACTGGCCACGACTGGCCTACTGGCCAACTGGCCGGCACTGGCCAACTGGCCACTGGCCGACTGGCCGTACTGGCCGACTGGCCCTCTCTGGACTACTGGCCGGACTGGCCGAACTGGCCTTTGACGTACTGGCCACTGGCCATCGCACTGGCCACTGGCCGATTACTGGCCACTGGCCACTGGCCACTGGCCTCACGAGTTACTGGCCGACTGGCCTTGAACTGGCCAACTGGCCACTGGCCACTGGCCGCGACTGGCCCACTGGCCTATTGACTGGCCACGACTGGCCAGTACTGGCCAAACTGGCCACTGGCCAATGTCCGGGTCGAACGGGACTGGCCTTACTGGCCACTGGCCATCTTTATATGTACTGGCCGCGACTGGCCAGACTGGCCACTGGCCAAACTGGCCACTGGCCAATTGGACTGGCCACTGGCCCTTATTTCATGACTGGCCTGCTTACTGGCCGACTGGCCACTGGCCGGGTTCTACACTGGCCGTTGACTGGCCGACTGGCCTCCATGCGACTGGCCCTTAACTGGCCACAACTGGCCGGACTGGCCCACCCACTGGCCAACTGGCCACTGGCCACTGGCCCCTACTGGCCACTGGCCAACTGGCCCCAATGAACTGGCCACTGGCCGCGCTACTGGCCGTACAAGTTTGGACTGGCCGGTGACTGGCCACTGGCCACTGGCCACGCAAGACTGGCCTGGACTGGCCCAAGACTGGCCCGCAGGTCCAGGACTGGCCCTACTGGCCACTGGCCACTGGCCAGGTGAACTGGCCTACTGGCCAACTGGCCAATAACTGGCCGCCACTGGCCACTGGCCCCGTTTACTGGCCACGACAATGTACTGGCCACTGGCCCACTGGCCACTGGCCGACTGGCCGTACTGGCCACTGGCCAACTGGCCGCTTACACTGGCCGGACTGGCCATACTGGCCACTGGCCCACTGGCCGTATTCTACTGGCCTTTGCACTGGCCACTGGCCCTACTGGCCGGACCAACTGGCCCACTGGCCACTGGCCTCCTACTGGCCCCAAACCACTGGCCGTACTGGCCGACTGGCCTACTGGCCCGGGGCACACTGGCCTAACGATGCGAAGGACTGGCCCCGCACTGGCCACTGGCCAACTGGCCAGCGGAACTGGCCACTGGCCACTGGCCGGACTGGCCTGGACTGGCCGAACTGGCCATACTGGCCACTGGCCGGGACTGGCCCACTGGCCAACTGGCCGTAATCACTGGCCAGACTGGCCACTGGCCGACTGGCCTATACGCACTGGCCAACTGGCCAACTGGCCACTGGCCTCTACTGGCCACTGGCCGTTTCCACTCACTGGCCCGAGCTCAGACTGGCCGACTGGCCGCACTGGCCTACTGGCCAGACTGGCCACTGGCCCAGACTGGCCAACTGGCCAGTACTGGCCCTACTGGCCAACTGGCCACTGGCCACTGGCCACGACTGGCCACTGGCCACTGGCCACTGGCCACCATACACCTACTGGCCTACTGGCCTGAATATGCCACTGGCCTCACTGGCCGACTGGCCATTATAGGACTGGCCTGGCAACTGGCCCGCCCTACTGGCCACTGGCCAACTGGCCACTGGCCACTGGCCTGCGACTGGCCAACTGGCCACCCACTGGCCTCATACTGGCCCGGAGAGATCGGCTAAACTGGCCACGACTGGCCCACTGGCCTCCGGCAACTGGCCACTGGCCACTGGCCTTGACTGGCCCAACTGGCCTTTACTGGCCACTGGCCACTGGCCTAATACTGGCCACTGGCCTTTATACTGGCCTTACTGGCCACTGGCCACTGGCCACTACTGGCCACTGGCCACTGGCCTTTACTGGCCATGAACTGGCCGACATGAACTGGCCACTGGCCTCTACTGGCCACGGCACTGGCCGCTCAACTGGCCCCAAACTGGCCACTGGCCCACTGGCCAGCACTGGCCACTGGCCAACTGGCCAACTGGCCACTACTGGCCGGAAGACTGGCCACTGGCCGTCTACTGGCCCGAACTGGCCACTGGCCACTGGCCACTGGCCGGACTGGCCACTGGCCTATACTGGCCTGATACTGGCCCACTGGCCACGACTGGCCAAACTGGCCTACTGGCCGGCGCTGGGCAGACTGGCCTCACACTGGCCATAACTGGCCAAGAGACTGGCCAACTGGCCAACTGGCCACTGGCCTCGTTGGACTGGCCGTAGACTGGCCTACTGGCCCACTGGCCACTGGCCAACTGGCCACTGGCCGCTACTGGCCAACTGGCCCCTTGACTGGCCGTAACTGGCCGGGACTGGCCTACTGGCCATTACTGGCCGAGGCACTGGCCGTGCACTGGCCTACTGGCCACTGGCCATCTCACTGGCCTCCGAACTGGCCACTGGCCTACTGGCCTACTGGCCTACTGGCCTTGAACTGGCCGCAACTGGCCGACTGGCCATCACTGGCCTACTGGCCGTTAAAACTGGCCTGAACTGGCCACTGGCCGCCCTACTGGCCAGACTGGCCACTGGCCACTGGCCTCATACTGGCCTTAACTGGCCAACTGGCCATACCCACTGGCCACTGGCCGGACTGGCCACTGGCCTCGACTGGCCAACTGGCCTTGAGAACTGGCCCACTGGCCCCACTGGCCTACTGGCCAGACTGGCCCGCGCAGCACTGGCCACTGGCCACGGACTGGCCACTGGCCGGACTGGCCTCTGTATTAGACTGGCCGCACTGGCCTACTGGCCACTGGCCCACTGGCCCTTCCATGCCCTCGACTGGCCACTACTGGCCCAACTGGCCATTCCAACTGGCCAGACAACTGGCCTTGGAAGGTTCTTACTGGCCACTGGCCCACTGGCCCACTGGCCTACTGGCCACTGGCCACTGGCCCTTTTCACTGGCCTAGACTGGCCACTGGCCTACTGGCCGATACTGGCCCGCCGGAGATCAGGACTGGCCACTGGCCGACTGGCCCGACTGGCCACTGGCCGAGTACTGGCCAAACTGGCCACTGGCCTACTGGCCCGCGAGACTGGCCTAACTGGCCACTGGCCACTGGCCTTTAATCTACACTGGCCCACTGGCCCCACTGGCCACTGGCCTTTGCCCTACTGGCCGGACTGGCCACTGGCCTTACTGGCCCCGAACTGGCCACTGGCCGAAACTGGCCACTGGCCGCTAAGCTCTCAAAACTGGCCAACTGGCCACTGGCCACTGGCCCACTGGCCCAGGACTGGCCGGCCACTGGCCCGCGTGCGACTGGCCACTGGCCAACTGGCCACTGGCCAACTGGCCGACTGGCCCAACTGGCCACTGGCCATCCCCCGAGGACTGGCCTACTGGCCGACTGGCCTACTGGCCGCACTGGCCCGGACTGGCCACTGGCCCCCACTGGCCAACTGGCCACTGGCCGGTGTTTGCACTGGCCTACACACTGGCCACTGGCCCTACTGGCCACTGGCCACTGGCCTGTACTGGCCTACTGGCCACTGGCCGACTGGCCTGCACTGGCCTAGCCACTGGCCAACTGGCCTACTAATCACTGGCCGTAACTGGCCACGACTGGCCTACTGGCCTGAGGAAGTCACTGGCCACTGGCCATGACTGGCCGGCAGAAACTGGCCCGAACCTAACTGGCCTAACTGGCCGACTGGCCAACTGGCCGACCACTGGCCACTGGCCACTGGCCACTGGCCGACTGGCCTGACTGGCCAGAGACTGGCCAACTGGCCACTGGCCACTGGCCGACTGGCCAAACTGGCCACTGGCCAACTGGCCGGACTGGCCACTGGCCTAACTGGCCACTGGCCACTGGCCACTGGCCACTGGCCTTATTGACTGGCCTAACTGGCCGACTGGCCTCCCTGCTCCTCGATTCGCGACTGGCCACTGGCCACTGGCCCAACGCACTGGCCCAAGCTCACTGGCCACTGGCCCACGACTGGCCTGACATAACTGGCCACGGACTGGCCAACTGGCCTCCTACTGGCCACTGGCCTACTGGCCCTACTGGCCTATACTGGCCATATTCACTGGCCGTGGACTGGCCGCACTGGCCGACTGGCCACTGGCCGATTCACTGGCCTTGTTACTGGCCATGATCGACTGGCCACTGGCCAGTGGTTTACTGGCCACTGGCCTGCACTGGCCAACTGGCCACTGGCCGACTGGCCGAACTTACTGGCCTACTGGCCGTTACGACTGGCCCACTGGCCAATCTGAATCACTGGCCCAACTGGCCACTGGCCGTACTGGCCTGAGCACTGGCCTACTGGCCTACTGGCCACTGGCCAAACTGGCCACTGGCCACTGGCCGACTGGCCAATACTGGCCAACTGGCCCACTGGCCAGACTGGCCGTACTGGCCTAATGACTGGCCACTGGCCCGTGACTGGCCCTTCACTGGCCACTGGCCACTGGCCCAGACTGGCCCACTGGCCGAAAAGATACTGGCCACTGGCCGCGTACTGGCCAACTGGCCAGTACTGGCCGGACTGGCCACTGGCCTCAACTGGCCCCACTGGCCGACTGGCCACTGGCCAACTGGCCGACTGGCCTATTTACTGGCCACTGGCCTTAGTTAACTGGCCCCTACTGGCCAATTCACTGGCCAACTGGCCGGGAATATCCACTGGCCCACTGGCCCCACTGGCCACACACTGCCACTGGCCCCTTACTGGCCGACTGGCCCCTACTGGCCCTGACTGGCCACTGGCCTTACTGGCCCACTGGCCACTGGCCACTGGCCACTACTGGCCCGCACTGGCCATCACTGGCCCGGTTGACTGGCCACTGGCCACAACTGGCCGTCACTGGCCCTGACTGGCCGGCGACTGGCCCTCGTAGACTGGCCCGTAACTGGCCAGACTGGCCATCTACTGGCCTACTGGCCTCACTGGCCCTCAACTGGCCCACGTAGTACTGGCCACTGGCCAACTGGCCACTGGCCTACTGGCCGAACTGGCCACTGGCCGACTGGCCTCTGGTGGACTGGCCTACTGGCCTTCCCACTGGCCCCAGACTGGCCCTCGTACTGGCCCACTGGCCTGAATACACTGGCCAACTGGCCACACTGGCCACTGGCCACTGGCCGATTGGCACTGGCCTGGAACTGGCCACTGGCCTTACTGGCCACTGGCCCACTGGCCCTTACTACTGGCCACTGGCCCTATACTGGCCACTGGCCACTGGCCAGACTGGCCACTGGCCACTGGCCCACGACTGGCCCCGGCCACTGGCCGTGACTGGCCCCTGACTGGCCGAGATAACTGGCCATACTGGCCTCCACTGGCCGACTGGCCAACTGGCCTGGACTGGCCCTGAACTGGCCACTGGCCACAACTGGCCCACGTTTGACTGGCCTGACTGGCCACTGGCCCTCATACTGGCCACTGGCCACTGGCCACTGGCCTCTACCACTGGCCGGCAAGGAACTGGCCTAGCACTGGCCGTTCTTCTACTGGCCTCACAACTGGCCACTGGCCGACTGGCCACTGGCCGCGCACTGGCCACTGGCCAAGTGACTGGCCACTGGCCACTGGCCGGACTGGCCACTGGCCCTAACTGGCCTCAGGAAACATACTGGCCCACTGGCCAGTGTATGAACTGGCCGATCTTACTGGCCACTGGCCTGCACTGGCCCACTGGCCTACTGGCCAATGAAACTGGCCACTGGCCACTGGCCACACTGGCCTTACCCACTGGCCACTGGCCCACTGGCCCCACTGGCCCGCACTGGCCGAACTGGCCCTTACTGGCCGACTGGCCACTGGCCACTGGCCTACTGGCCGGCACTGGCCAAACTGGCCGTAACTGGCCACAAGAGTGCAGAGACTGGCCTACTGGCCGGCGCACTGGCCCGACTGGCCATGACTGGCCACTGGCCGACTGGCCCACTGGCCGACAGTACTGGCCGACTGGCCAACTGGCCTACAACTGGCCAGGTAACTGGCCATACTGGCCACTGGCCGAACGTACTGGCCACTAACTGGCCACACTGGCCAACTGGCCGACTGGCCGACCAACTGGCCCATGACTGGCCACTGGCCACTGGCCGACTGGCCCGAATATACAGGTACTGGCCAACTGGCCATCGATACTGGCCATCAACTGGCCACTGGCCTCACTGGCCAACTGGCCATACTGGCCGCCCCTGACTGGCCAGATGTTACTGGCCACTGGCCACTGGCCACTGGCCACTGGCCCGACTGGCCGGCCTCTACCGGGACTGGCCTGACTGGCCGTAACTGGCCGGCGACACTGGCCCAAGTAACTGGCCTGCGAGACTGGCCAATTCACTGGCCGACTGGCCCCACTGGCCCACTGGCCTGCTACTGGCCACTGGCCTTACTGGCCAAAAAAGGACACTGGCCTACTGGCCCCTATACTGGCCGACTGGCCACTGGCCGATCACTGGCCACACTGGCCACTGGCCTTTAAGACTGGCCACTGGCCAACTGGCCACTGGCCACTGGCCACTGGCCGAACTGGCCTACTGGCCACTGGCCGGCACTGGCCAATTCACTGGCCGAGGACTGGCCATGATACTGGCCTAAAGACTGGCCACTGGCCACCACTGGCCACTGGCCCACTGGCCCATACTGGCCCAGACTGGCCGTTTTGATCATTGACTGGCCACTGGCCAACTGGCCACTGGCCCCTCGTACTGGCCGGAACTGGCCTGGTTACTGGCCACTGGCCACTGGCCACTATACTGGCCAACTGGCCCGCGCAACTGGCCACACTGGCCGCTTATACTGGCCGCCACTGGCCACTGGCCGTTACTGGCCAAGCACTGGCCTCTTACTGGCCTACTGGCCCGACTGGCCCACTGGCCCTTACTGGCCACTGGCCTAACTGGCCACTGGCCCACACTGGCCTTCCTACTGGCCACTGGCCACTGGCCACACTGGCCATCGCTCCTAACTGGCCTCTTTAAACTGGCCGTATGACTGGCCACTGGCCACCCACTGGCCGCGACTGGCCAACTGGCCACTGGCCTACACTGGCCCAAACTGGCCACTGGCCCGGTGGTGACTGGCCAACTGGCCTACTGGCCGAGACTGGCCACTGGCCAACTGGCCAGACTGGCCTACTGGCCACTGGCCGGACTGGCCGAAATTACTGGCCCACTGGCCGTACTGGCCGCGGACTGGCCACTGGCCAACTGGCCACTGGCCCCTGTTACATTGTAACTGGCCTCAACTGGCCACTGGCCACTGGCCACTGGCCTCTATTACTGGCCCCTTGGATAAACGCACTGGCCACTGGCCTCGTACTGGCCACACTGGCCCACTGGCCTGACTGGCCACTGGCCCAGCAAACTGGCCAACTGGCCACTGGCCACTGGCCCTT'

print pattern_matching('ATGATCAAG', genome)
            