'''
Global and local alignment
Global:
     Input: Two protein strings written in the single-letter amino acid alphabet.
     Output: The maximum alignment score of these strings followed by an alignment achieving this
     maximum score. Use the BLOSUM62 scoring matrix and indel penalty sigma = 5.
Local:
     Input: Two protein strings written in the single-letter amino acid alphabet.
     Output: The maximum score of a local alignment of the strings, followed by a local alignment of these
     strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty sigma = 5.
'''
import urllib2

def compute_scoring_matrix(global_flag):
    """
    Global_flag = True: global alignment. BLOSUM62 matrix
    Global_flag = False: local alignment. PM250 matrix
    """
    scoring_dict = {}
    if global_flag:
        scoring_file = urllib2.urlopen('https://stepic.org/media/attachments/lessons/247/BLOSUM62.txt')
    else:
        scoring_file = urllib2.urlopen('https://stepic.org/media/attachments/lessons/247/PAM250_1.txt')

    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
        
    return scoring_dict

def compute_alignment_matrix(seq1, seq2, scoring_matrix, global_flag):
    
    """
    Use Dynamic Programming to find optimal alignment. Save in list
    Global_flag = True: global alignment
    Global_flag = False: local alignment. If alignment score < 0, make it = 0
    """
    alignment_matrix = []
    alignment_matrix.append([])
    alignment_matrix[0].append(0)
    
    for length in range(1, len(seq_x) + 1):
        alignment_matrix.append([])
        value = alignment_matrix[length-1][0] - indel_penalty 
        
        if value < 0 and not global_flag:
            alignment_matrix[length].append(0)
        else:
            alignment_matrix[length].append(value)  
        
    for length in range(1, len(seq_y) + 1):
#        print length,alignment_matrix[0][length-1]
        value = alignment_matrix[0][length-1] - indel_penalty 
        
        if value < 0 and not global_flag:
            alignment_matrix[0].append(0)
        else:
            alignment_matrix[0].append(value)
        
    for len_x in range(1, len(seq_x) + 1):
        for len_y in range(1, len(seq_y) + 1):
            value = max(alignment_matrix[len_x-1][len_y-1] + scoring_matrix[seq_x[len_x - 1]][seq_y[len_y - 1]],
                        alignment_matrix[len_x-1][len_y] - indel_penalty ,
                        alignment_matrix[len_x][len_y-1] - indel_penalty )
            
            if value < 0 and not global_flag:
                alignment_matrix[len_x].append(0)
            else:
                alignment_matrix[len_x].append(value)
              
#    for i in range(len_x + 1):
#        print alignment_matrix[i]
    return alignment_matrix


def compute_global_alignment(seq_x, seq_y):
    """
    Global alignment. Track back from the last element of the matrix.
    Length of the returned aligned sequence = longer one of the two
    """
    scoring_matrix = compute_scoring_matrix(True)
    alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, True)
    
    align_x = ''
    align_y = ''
    len_x = len(seq_x) 
    len_y = len(seq_y) 
    
    while len_x > 0 and len_y > 0: # If seq = '' len_x is -1
#        print alignment_matrix[len_x][len_y]
        if alignment_matrix[len_x][len_y] == alignment_matrix[len_x-1][len_y-1] + scoring_matrix[seq_x[len_x-1]][seq_y[len_y-1]]:
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
            
    while len_x > 0:
        align_x = seq_x[len_x-1] + align_x
        align_y = '-' + align_y
        len_x -= 1
    while len_y > 0:
        align_x = '-' + align_x
        align_y = seq_y[len_y-1] + align_y
        len_y -= 1    
        
    print alignment_matrix[len(seq_x)][len(seq_y)]
    print align_x
    print align_y
    


def compute_local_alignment(seq_x, seq_y):
    """
    Local alignment. 
    Track back from the element with max score of the matrix.
    Stop at alignment_score = 0 (not included)
    So '-' should not be at the beginning
    Length of the returned aligned sequence = shorter one of the two
    """
    scoring_matrix = compute_scoring_matrix(False) 
    alignment_matrix = compute_alignment_matrix(seq_x, seq_y, scoring_matrix, False)
#    x = max(alignment_matrix[len_x][len_y] for len_x in range(len(seq_x)) for len_y in range(len(seq_y)) )
#    y = alignment_matrix.index(x)
    max_score = 0
    max_len_x = 0
    max_len_y = 0
#    for i in range(len(seq_x) + 1):
#        print alignment_matrix[i]
    for len_x in range(0, len(seq_x) + 1):
        for len_y in range(0, len(seq_y) + 1):
#            print len_x, len_y, alignment_matrix[len_x][len_y]
            if alignment_matrix[len_x][len_y] > max_score:
                max_score = alignment_matrix[len_x][len_y]
                max_len_x = len_x
                max_len_y = len_y
                
    align_x = ''
    align_y = ''
    len_x,len_y = max_len_x,max_len_y
    while alignment_matrix[len_x][len_y] > 0:
        if alignment_matrix[len_x][len_y] == alignment_matrix[len_x-1][len_y-1] + scoring_matrix[seq_x[len_x-1]][seq_y[len_y-1]]:
            align_x = seq_x[len_x-1] + align_x
            align_y = seq_y[len_y-1] + align_y
            len_x -= 1
            len_y -= 1
        elif alignment_matrix[len_x][len_y] == alignment_matrix[len_x-1][len_y] - indel_penalty:
            align_x = seq_x[len_x-1] + align_x
            align_y = '-' + align_y
            len_x -= 1
        else: # alignment_matrix[len_x][len_y] == alignment_matrix[len_x][len_y-1] + scoring_matrix['-'][seq_y[len_y]]:
            align_x = '-' + align_x
            align_y = seq_y[len_y-1] + align_y
            len_y -= 1
    ''' 
    DO NOT ADD THIS!!!
    while len_x > 0:
        align_x = seq_x[len_x-1] + align_x
        align_y = '-' + align_y
        len_x -= 1
    while len_y > 0:
        align_x = '-' + align_x
        align_y = seq_y[len_y-1] + align_y
        len_y -= 1  
    '''        
    score = 0
    for idx in range(len(align_x)):
        if align_x[idx] == '-' or align_y[idx] == '-':
            score -= indel_penalty
        else:
            score += scoring_matrix[align_x[idx]][align_y[idx]]
        if score < 0:
            score = 0
    
    print score
    print align_x
    print align_y

indel_penalty = 5

seq_y = 'PLEASANTLY'
seq_x = 'MEANLY'

compute_local_alignment(seq_x, seq_y)