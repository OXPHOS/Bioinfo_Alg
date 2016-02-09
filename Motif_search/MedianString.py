'''
Use Brute Force Method
Generate a list of all possible median strings of length k
Calculate the min score of d(pattern, motif) in each string
Then sum up the score of all string
'''


CODE = {'A':0,'C':1,'G':2,'T':3}

def code_to_dna(value, k):
    #Convert number to text
    code_r = {0:'A', 1:'C', 2:'G', 3:'T'}
    seq_r = ''
    
    while len(seq_r) < k:
        seq_r =  code_r[value % 4] + seq_r
        value  = value // 4
    return seq_r

def kmer_generation(k):
    # Generate all kmer via Quaternary numbers
    global pattern
    pattern = []
    for _ in range(4**k):
        pattern.append(code_to_dna(_, k))
    return

def alignment(seq1, seq2):
    # Align a kmer with a dna string, return the minimum score 
    scores = []
    for i in range(0, len(seq2) - len(seq1) + 1):
        score = 0
        for j in range(len(seq1)):
            if seq1[j] != seq2[i + j]:
                score += 1
        scores.append(score)
    return min(scores)
            

def medianstring_search(Dna, k):
    
    dna_strings = []
    for line in Dna.splitlines():
#        print line.strip()
        dna_strings.append(line.strip( ))
            
    kmer_generation(k)
    median = ''
    dmin = k * len(dna_strings)
    for motif in pattern:
        dist = 0
        for string in dna_strings:
            dist += alignment(motif, string)
        if dist < dmin:
            print dist, dmin, motif
            dmin = dist
            median = motif
    return median
        

Dna = '''AAAGCCCAATTTCGAATCAGGCCCAGATGGGCATTCAGTTTG
ATGTAAACGTGAAGACGGAGCCATTATATCCACACCCTCTGT
CAAAAAGTTCTTATCCGTTCTCGCAGATGGGAACCTTAACTA
TTGAGGACTTTTCTATTTTGGTTGCTCACGCCGTGTAGATGG
GAAAAAAGACGGACTAACGAATACGAGCACCCTCAAAGGTTA
AGATGGGCTGCGCCGCTACATTATACTTTCTAGCATGGTACA
GATAAATCTCTTAGACGGATAACCGGCTTTAGACTAGTTGTT
AGATGGCAAATAGCTGTATCACTCCATATGTCTAATTTGCTC
AGATGGATCGTCGCAGGATCGGGTCAGTTCACCGTACCCCCT
CCAAAAAGAAGGAGCATGGCGTATATTCTCGAGTCGTTCAGC
'''

print medianstring_search(Dna, 6)
