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
    

def calculate_score(motifs, matrix, k, t):
    '''
    Calculate the score of kmer cluster based on one most likely kmer(median_motif)
    '''
    median_motif = ''
    score = 0
    
    for i in range(k):
        prob = [matrix[_][i] for _ in range(4)]
        median_motif += CODE_R[prob.index(max(prob))]
    print median_motif
    
    for i in range(t):
        for j in range(k):
            if median_motif[j] != motifs[i][j]:
                score += 1
    return score

motifs = ['TCTCGGGG','CCAAGGTG','TACAGGCG','TTCAGGTG','TCCACGTG']
matrix = calculate_prob_matrix(motifs, 8, 5)
print calculate_score(motifs, matrix, 8, 5)


'''
TCCAGGTG
9
'''