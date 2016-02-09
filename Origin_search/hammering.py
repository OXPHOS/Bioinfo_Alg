"""
Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k <= 12 and d <= 3.
     Output: All most frequent k-mers with up to d mismatches in Text.

Giving a piece of sequence seq, kmer k, mismatch tolerance d,
Find out the pattern kmer with maximum repeats by hash algorithm
k <= 12, d <= 3


Hand convert file: http://www.codeskulptor.org/#user38_4NXGL2qpa0_2.py
"""


CODE = {'A':0,'C':1,'G':2,'T':3}
KMERS = set()


#*************************HASH ALGORITHM*************************#
def code_convert(text, k):
    'Convert number to text'
    code_r = {0:'A', 1:'C', 2:'G', 3:'T'}
    seq_r = ''

    while len(seq_r) < k:
        seq_r =  code_r[text % 4] + seq_r
        text  = text // 4
    return seq_r

def mismatch_values(kmer_value, k, d):
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

"""
#test = list(mismatch_values(27, 4, 1))   #'ACGT'
test = list(mismatch_values(11, 4, 3))    #'AAGT'
print '1', test
for _ in test:
    print code_convert(_, 4)
"""
    
def hammering_pattern_hash(seq, k, d):
    '''
    Main part
    1. Convert seq to kmer number values by order
    2. Calculate the kmer mismatched sequences' number
    3. Reverse complement seq is considered
    4. Find out the kmer that has been repeated most times
    '''
    global KMERS
    pattern = [0] *(4**k)
    kmer_value = 0
    kmer_value_reverse = 0
    #Initialize value
    for i in range(k):
        kmer_value = (kmer_value << 2) + CODE[seq[i]]
        kmer_value_reverse = (kmer_value_reverse << 2) + 3 - CODE[seq[k - i - 1]] ###ANY OTHER WAY??
    #Add first kmer
    hammering_value = mismatch_values(kmer_value, k, d)
    for _ in hammering_value:
        pattern[_] += 1
    hammering_value_reverse = mismatch_values(kmer_value_reverse, k, d)
    for _ in hammering_value_reverse:
        pattern[_] += 1
#    pattern[i for i in hammering_value] += 1

    #Calculate further kmers
    kmer_mask = 4 ** (k - 1) - 1 #00xxxxxx
    kmer_mask_reverse = 4 ** k - 1 - 3
    for i in range(1, len(seq) - k + 1):
        kmer_value = ((kmer_value & kmer_mask) << 2) +  CODE[seq[i + k - 1]]
        hammering_value = mismatch_values(kmer_value, k, d)
        for _ in hammering_value:
            pattern[_] += 1
        
        kmer_value_reverse = ((kmer_value_reverse & kmer_mask_reverse) >> 2) +  ((3 - CODE[seq[i + k - 1]]) << 2 * (k - 1))
        hammering_value_reverse = mismatch_values(kmer_value_reverse, k, d)
        for _ in hammering_value_reverse:
            pattern[_] += 1
#        pattern[reverse_constant - int(reading_frame[::-1])] += 1  ###Convert a string
        
    max_rep = max(pattern)
    
    for idx in range(len(pattern)):
#        print idx, pattern[idx], code_convert(idx, k)
        if pattern[idx] == max_rep:            
            KMERS.add(code_convert(idx, k))

       


#*************************BRUTE FORCE*************************#
def hammering_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        print 'Error! Unequal length'
        exit()
        
    ham_dist = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            ham_dist += 1
#    print ham_dist
    return ham_dist

def hammering_pattern_search_BF(text, k, mismatch):
    count_list = []
    for code in range(4**k - 1):
        pattern = code_convert(code, k)
        count = 0
        for i in range(len(text) - k + 1):
            if hammering_distance(text[i:i+len(pattern)], pattern) <= mismatch:
                count += 1
        count_list.append(count)
    
    max_count = max(count)
    for i in range(len(text) - k + 1):
#        print i, count[i], text[i:i+k]

        if count[i] == max_count:
            print i #, text[i:i+k]
            KMERS.add(text[i:i+k])
    return 

            
pattern_seq = 'ACGTTGCATGTCGCATGATGCATGAGAGCT' #4, 1A
genome_seq =  'GCCGACGAGCCGACGACGAGGGGCGGGGGGGTAGCAGGGGCCGAGCACGAGGGGCGTAGTAGGGGGGGCGCGTAGCAGTAGCGCGCAGTAGGGGCGTACGAGCGTACGAGCGCACGAGTAGCCGACGACGAGCGGGGGGGCACGAGGGGTAGGGGGGCGACGAGTAGTAGGGCGAGCACGAGCACGAGCGTAGGGGCAGCGGGGTACGAGGGGGGCGAGTAGCGCGCGGGCGAGCGGGCGAGCGTA'
#pattern_search_BF('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)
hammering_pattern_hash(genome_seq, 10, 2)
#hammering_pattern_hash(pattern_seq, 4, 1)

print KMERS