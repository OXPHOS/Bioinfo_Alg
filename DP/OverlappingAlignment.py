'''
Overlapping Alignment
     Input: Two strings v and w, each of length at most 1000.
     Output: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v' of
     v and a prefix w' of w achieving this maximum score. Use an alignment score in which matches count
     +1 and both the mismatch and indel penalties are 2.

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
            value = max(alignment_matrix[len_x-1][len_y-1] + 3 * (int(seq_x[len_x - 1] == seq_y[len_y - 1])) - indel_penalty,
                        alignment_matrix[len_x-1][len_y] - indel_penalty,
                        alignment_matrix[len_x][len_y-1] - indel_penalty )

            alignment_matrix[len_x].append(value) 

#    for i in range(len_x + 1):
#        print alignment_matrix[i]
    return alignment_matrix


def compute_overlapping_alignment(seq_x, seq_y):
    
    alignment_matrix = compute_alignment_matrix(seq_x, seq_y)
    
    align_x = ''
    align_y = ''
    
    '''
    Start from the most down x axis with the max score (when align suffix of x and prefix of y)
    '''
    max_score = -100
    max_len_x = len(seq_x) 
    max_len_y = 0
    for len_y in range(len(seq_y), -1, -1):   ### Thus the alignment prefer dismatch than indel
#        print len_x, alignment_matrix[len_x][max_len_y]
        if alignment_matrix[max_len_x][len_y] > max_score:
            max_score = alignment_matrix[max_len_x][len_y]
            max_len_y = len_y
    len_x,len_y = max_len_x,max_len_y
    print max_score
    
    '''
    Backtrack suffix of x and prefix of y
    '''
    while len_x > 0 and len_y > 0: # If seq = '' len_x is -1
        if (alignment_matrix[len_x][len_y] == alignment_matrix[len_x-1][len_y-1] + 3 * (int(seq_x[len_x - 1] == seq_y[len_y - 1])) - indel_penalty):
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

    print align_x
    print align_y


indel_penalty = 2


seq_x = 'PAWHEAE'
seq_y = 'HEAGAWGHEE'

compute_overlapping_alignment(seq_x, seq_y)