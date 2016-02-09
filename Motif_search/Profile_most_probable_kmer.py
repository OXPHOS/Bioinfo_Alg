'''
Given a probability matrix and the k value of k-mer,
Find the k-mer with highest probability in the DNA string
'''

global k

def generate_profile_matrix(scores):
    # Convert probability matrix string into dictionary. Key = nt
    global matrix
    matrix = {}
    
    nucleotides = ['A', 'C', 'G', 'T']
    lines = []
    for line in scores.splitlines():
        line = line.strip()
        lines.append(map(float, line.split(' ')))
    for i in range(4):
        matrix[nucleotides[i]] = lines[i]
    return

def profile_most_probable_kmer(dna):
    pmax = 0
    candidate = dna[0: k]
    for i in range(len(dna) - k + 1):
        p = 1
        for j in range(k):
            p *= matrix[dna[i + j]][j]
        if p > pmax:
            pmax = p
            candidate = dna[i: i + k]
    return candidate

input_matrix = '''0.364 0.333 0.303 0.212 0.121 0.242
0.182 0.182 0.212 0.303 0.182 0.303
0.121 0.303 0.182 0.273 0.333 0.303
0.333 0.182 0.303 0.212 0.364 0.152'''

generate_profile_matrix(input_matrix)
k = 6
print profile_most_probable_kmer('TGCCCGAGCTATCTTATGCGCATCGCATGCGGACCCTTCCCTAGGCTTGTCGCAAGCCATTATCCTGGGCGCTAGTTGCGCGAGTATTGTCAGACCTGATGACGCTGTAAGCTAGCGTGTTCAGCGGCGCGCAATGAGCGGTTTAGATCACAGAATCCTTTGGCGTATTCCTATCCGTTACATCACCTTCCTCACCCCTA')
