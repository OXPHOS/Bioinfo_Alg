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

def generate_prob_random_motif(matrix, seq, k, t):
    prob_list = [0]
    sum = 0.0
    for i in range(len(seq) - k + 1):
        p = 1.0
        for j in range(k):
            p *= matrix[CODE[seq[i + j]]][j]
        sum += p
        prob_list.append(sum)
    prob_list = [prob_list [_] / sum for _ in range(len(prob_list))]
    
#    for i in range(len(prob_list) - 1):
#        print prob_list[i + 1], seq[i: i + k]
    
    random_value = random.random()
#    print random_value
    for i in range(len(prob_list) - 1):
        if random_value > prob_list[i] and random_value < prob_list[i + 1]:
            return seq[i: i + k]
            
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
#    print 'median_motif=',median_motif
    
    for i in range(t):
        for j in range(k):
            if median_motif[j] != motifs[i][j]:
                score += 1
    return score

def gibbs_sampler(Dna, k, t, N):
    # Separate DNA strings
    dna_strings = []
    for line in Dna.splitlines():
#        print line.strip()
        dna_strings.append(line.strip( ))
  
    # Initiate
    l = len(dna_strings[0])
    index = [random.randrange(l - k + 1) for _ in xrange(t)]
    motifs = [dna_strings[_][index[_] : index[_] + k] for _ in xrange(t)]
    best_motifs = motifs
    matrix = calculate_prob_matrix(motifs, k, t)
    best_score =  calculate_score(motifs, matrix, k ,t)
    
    # Iterate to get a motif pattern with min score
    for j in xrange(N):
        
        # Calculate profile matrix, motifs with min scores and socres
        i = random.randrange(t)
        matrix_i = calculate_prob_matrix(motifs[0 : i] + motifs[i + 1 : ], k, t - 1)
        motifs[i] = generate_prob_random_motif(matrix_i, dna_strings[i], k, t)
        #motifs[i] = profile_most_probable_kmer(matrix_i, dna_strings[i], k) NO ROLL-DIE
#        print 'picked i =', i, motifs[i]
        matrix = calculate_prob_matrix(motifs, k, t)
        score = calculate_score(motifs, matrix, k, t)
        
#        print score, motifs
        if score < best_score:
            best_score = score
            best_motifs = motifs
            
    print best_score
    calculate_score(best_motifs, calculate_prob_matrix(best_motifs, k, t), k, t)           
    return best_motifs
    


Dna = '''CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
     GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
     TAGTACCGAGACCGAAAGAAGTATACAGGCGT
     TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
     AATCCACCAGCTCCACGTGCAATGTTGGCCTA'''


best_motifs = gibbs_sampler(Dna, 8, 5, 10000) # Cannot work out correct score = 9

output = ''
for motif in best_motifs:
    output = output + motif + '\n'
print output.strip()


