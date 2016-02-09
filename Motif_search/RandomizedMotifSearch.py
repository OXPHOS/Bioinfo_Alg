'''
#Iterate to generate best hit motifs with randomized method

#RANDOMIZEDMOTIFSEARCH(Dna, k, t)
#    randomly select k-mers Motifs = (Motif1, ..., Motift) in each string
#        from Dna
#    BestMotifs <- Motifs
#    while forever
#        Profile <- Profile(Motifs)
#        Motifs <- Motifs(Profile, Dna)
#        if Score(Motifs) < Score(BestMotifs)
#            BestMotifs <- Motifs
#        else
#            return BestMotifs
'''

import random

CODE = {'A':0,'C':1,'G':2,'T':3}
CODE_R = {0:'A', 1:'C', 2:'G', 3:'T'}


def calculate_prob_matrix(motifs, k, t):
    '''
    Profile   A:  .2  .2   0   0   0   0  .9  .1  .1  .1  .3   0            
              C:  .1  .6   0   0   0   0   0  .4  .1  .2  .4  .6  
              G:   0   0   1   1  .9  .9  .1   0   0   0   0   0  
              T:  .7  .2   0   0  .1  .1   0  .5  .8  .7  .3  .4  
    '''
    matrix = [[1.0 / (t + 4)] * k, [1.0 / (t + 4)] * k, [1.0 / (t + 4)] * k, [1.0 / (t + 4)] * k] 
    for i in range(k):
        for j in range(t):
            matrix[CODE[motifs[j][i]]][i] += 1.0/ (t + 4)
#    print matrix
    return matrix

def profile_most_probable_kmer(matrix, string, k):
    '''
    According to current profile, identify the most possible kmer in one DNA string
    '''
    pmax = 0
    candidate = string[0: k]
    for i in range(len(string) - k + 1):
        p = 1
        for j in range(k):
            p *= matrix[CODE[string[i + j]]][j]
        if p > pmax:
            pmax = p
            candidate = string[i: i + k]
    return candidate

def calculate_score(motifs, matrix, k, t):
    '''
    Calculate the score of kmer cluster based on one most likely kmer(median_motif)
    '''
    median_motif = ''
    score = 0
    
    for i in range(k):
        prob = [matrix[_][i] for _ in range(4)]
        median_motif += CODE_R[prob.index(max(prob))]
    
    for i in range(t):
        for j in range(k):
            if median_motif[j] != motifs[i][j]:
                score += 1
    return score

def randomized_motif_search(Dna, k, t):
    # Separate DNA strings
    dna_strings = []
    for line in Dna.splitlines():
#        print line.strip()
        dna_strings.append(line.strip( ))
    
    
    l = len(dna_strings[0])
    best_score = t * k
    best_motifs = []
    
    # Run 1000 random simulations
    for _ in range(1000):
        
        # Initiate
        index = [random.randrange(l - k + 1) for _ in xrange(t)]
        curr_best_motifs = [dna_strings[_][index[_] : index[_] + k] for _ in xrange(t)]
        matrix = calculate_prob_matrix(curr_best_motifs, k, t)
        curr_best_score =  calculate_score(curr_best_motifs, matrix, k ,t)
        
        # Iterate to get a motif pattern with min score
        while True:
            # Calculate profile matrix, motifs with min scores and socres
            matrix = calculate_prob_matrix(curr_best_motifs, k, t)
            motifs = []
            for _ in xrange(t):
                motifs.append(profile_most_probable_kmer(matrix, dna_strings[_], k))
            score = calculate_score(motifs, matrix, k, t)
            
            if score < curr_best_score:
                curr_best_score = score
                curr_best_motifs = motifs
            else:
                break
                
        # Compare each simulation
        if curr_best_score < best_score:
            best_score = curr_best_score
            best_motifs = curr_best_motifs
            
    print best_score            
    return best_motifs
    


Dna = '''CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
     GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
     TAGTACCGAGACCGAAAGAAGTATACAGGCGT
     TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
     AATCCACCAGCTCCACGTGCAATGTTGGCCTA'''

best_motifs = randomized_motif_search(Dna, 8, 5)

output = ''
for motif in best_motifs:
    output = output + motif + '\n'
print output.strip()


