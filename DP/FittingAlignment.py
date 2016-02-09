'''
Fitting Alignment
     Input: Two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100.
     Output: A highest-scoring fitting alignment between v and w. Use the simple scoring method in which
     matches count +1 and both the mismatch and indel penalties are 1
The total length is the same as the shorter sequence.
Actually the score was deduced from len(seq_shorter) whereever there's a mismatch or indel
'''
import urllib2


def compute_alignment_matrix(seq1, seq2):
    
    """
    Use Dynamic Programming to find optimal alignment. Save in list

    """
    
    alignment_matrix = []
    alignment_matrix.append([])
    alignment_matrix[0].append(0)
    for length in range(1, len(seq_x) + 1):
        alignment_matrix.append([])
        value = alignment_matrix[length-1][0]    ####KEY to the Fitting Scoring. No penalty if y = 0
        alignment_matrix[length].append(value)  
        
    for length in range(1, len(seq_y) + 1):
#        print length,alignment_matrix[0][length-1]
        value = alignment_matrix[0][length-1] - indel_penalty 
        alignment_matrix[0].append(value)
        
    for len_x in range(1, len(seq_x) + 1):
        for len_y in range(1, len(seq_y) + 1):
            value = max(alignment_matrix[len_x-1][len_y-1] + 2 *indel_penalty * (int(seq_x[len_x - 1] == seq_y[len_y - 1])) - indel_penalty,
                        alignment_matrix[len_x-1][len_y] - indel_penalty,
                        alignment_matrix[len_x][len_y-1] - indel_penalty )

            alignment_matrix[len_x].append(value)

    for i in range(len_x + 1):
        print alignment_matrix[i]
    return alignment_matrix


def compute_fitting_alignment(seq_x, seq_y):
    alignment_matrix = compute_alignment_matrix(seq_x, seq_y)
    
    align_x = ''
    align_y = ''
    
    '''
    Start from the most right y axis with the max score (when seq_y is shorter)
    '''
    max_score = 0
    max_len_x = 0
    max_len_y = len(seq_y)
    for len_x in range(0, len(seq_x) + 1):
#        print len_x, alignment_matrix[len_x][max_len_y]
        if alignment_matrix[len_x][max_len_y] > max_score:
            max_score = alignment_matrix[len_x][max_len_y]
            max_len_x = len_x
    len_x,len_y = max_len_x,max_len_y
    
    '''
    Backtrack two aligned seq with the same length of seq_y
    '''
    while len_x > 0 and len_y > 0: # If seq = '' len_x is -1
#        print alignment_matrix[len_x][len_y]
        if (alignment_matrix[len_x][len_y] == alignment_matrix[len_x-1][len_y-1] + 2 *indel_penalty * (int(seq_x[len_x - 1] == seq_y[len_y - 1])) - indel_penalty):
            align_x = seq_x[len_x-1] + align_x
            align_y = seq_y[len_y-1] + align_y
            len_x -= 1
            len_y -= 1
        elif alignment_matrix[len_x][len_y] == alignment_matrix[len_x-1][len_y] - indel_penalty :
            align_x = seq_x[len_x-1] + align_x
            align_y = '-' + align_y
            len_x -= 1
        else: # alignment_matrix[len_x][len_y] == alignment_matrix[len_x][len_y-1] + scoring_matrix['-'][seq_y[len_y]]:
            align_x = '-' + align_x
            align_y = seq_y[len_y-1] + align_y
            len_y -= 1
            

    while len_y > 0:
        align_x = '-' + align_x
        align_y = seq_y[len_y-1] + align_y
        len_y -= 1  
    
    score = 0
    for idx in range(len(align_x)):
        if (align_x[idx] == '-') or (align_y[idx] == '-') or (align_x[idx] != align_y[idx]):
            score -= indel_penalty
        else:
            score += 1
        if score < 0:
            score = 0
            
    print score
    print align_x
    print align_y


indel_penalty = 1

seq_x = 'GTAGGCTTAAGGTTA'
seq_y = 'TAGATA'

seq_x = 'PLEASANTLY'
seq_y = 'MEANLY'


compute_fitting_alignment(seq_x, seq_y)