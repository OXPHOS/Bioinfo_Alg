'''
Brute force method to search conservative k-mer motif in t given DNA string
motif exists in every string
the tolerance of motif mismatch is d. 
Which means if a k-mer is within d-nt different from the motif, the k-mer is taken as a motif

Use Breadth-First search to generate all the possible motifs(neighbors) of the 1st string.
Then use these neighbors as seeds to identify which neighbor's neighbor appears in every string.
'''


CODE = {'A':0,'C':1,'G':2,'T':3}

def dna_to_code(seq_nt):
    #Transform nucleotide to codes
    seq_num = ''
    for nt in seq_nt:
        seq_num += str(CODE[nt])
#    print seq_num
    return seq_num

def code_to_dna(value, k):
    'Convert number to text'
    code_r = {0:'A', 1:'C', 2:'G', 3:'T'}
    seq_r = ''

    while len(seq_r) < k:
        seq_r =  code_r[value % 4] + seq_r
        value  = value // 4
    return seq_r
        

def neighbor_generation(kmer_value, k, d):
    '''
    Use breath-first search-like method to find out the set with sequences 
    that are within d substitution compared to kmer
    '''
    
    value_list = [kmer_value]
    return_value_set = set([kmer_value])

    round = 1
    while round <= d:
        value_list_temp = []
        for temp in value_list:
#            print round, temp
            for i in range(k):
                for _ in range(1, 4):
                    new_value = temp ^  (_ << 2 * i)
                    if new_value not in return_value_set:
                        value_list_temp.append(new_value)
                        return_value_set.add(new_value)
#                    print new_value

            
        value_list = list(value_list_temp)
#        print len(value_list), round
        round += 1
#    print len(return_value_set)
    return return_value_set

def motifenumeration(Dna, k, d):
    # Transform letter to codes
    dna_strings = []
    for line in Dna.splitlines():
#        print line.strip()
        dna_strings.append(dna_to_code(line.strip( )))
    
    # Transform code to binary numbers
    dna_kmer_values = []
    for string in dna_strings:
        # Calculate Binary Value for each Kmer in each dna string
#        print string
        dna_kmer_values.append(set())
        kmer_value = 0
        #Initialize value
        for i in range(k):
            kmer_value = (kmer_value << 2) + int(string[i])
        dna_kmer_values[-1].add(kmer_value)
        
        #Calculate further kmers
        kmer_mask = 4 ** (k - 1) - 1 #00xxxxxx
        for i in range(1, len(string) - k + 1):
            kmer_value = ((kmer_value & kmer_mask) << 2) +  int(string[i + k - 1])
            dna_kmer_values[-1].add(kmer_value)
        
#        print dna_kmer_values[-1]
    
    # Generate kmer neighboring list
    ref = dna_kmer_values[0]
    neighbor_set_ref = set([])
    for value_ref in ref:
        neighbor_set_ref.update(neighbor_generation(value_ref, k, d))
    
    # Identify motif within d in the sequences
    motifs = set()
    for neighbor_ref in neighbor_set_ref:
        fit = 0
        # Generate new neighbor set from the known neighbor from the 1st seq
        neighbor_set = neighbor_generation(neighbor_ref, k, d)
#        print code_to_dna(neighbor_ref, k), neighbor_set
        for i in range(1, len(dna_strings)):
            if neighbor_set.intersection(dna_kmer_values[i]) != set([]):
                fit += 1        
        if fit == len(dna_strings) - 1:
            motifs.add(neighbor_ref)
    
    results = ''
    for motif in motifs:
        results += str(code_to_dna(motif, k)) + ' '
    print results
    
    

 
Dna ='''CTGGAGCTCGGCGAGACTATACAAG
GGTGGTTGTACCCGCTGGACCCGAC
GTGGATCGACCCACTTTATCGGATC
CCATCTCTGTCCGTAGCGACTAGGA
ACGAGCCATTGAGAGCAATCGCGAC
AGAACTAGGTAATAGACGACTGAGT'''
     
motifenumeration(Dna, 5, 2)
        
        
                 