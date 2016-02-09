def MahattanTourist(seq1, seq2):
    '''
    Dynamic programing
    n, m: number of nodes on x and y direction respectively.
    '''
    n = len(seq1)
    m = len(seq2)
    seq1 = '1' + seq1
    seq2 = '2' + seq2

    values = [[]]
    values[0].append(0)
    path = [[0]]
    for i in range(1, n + 1):
        values.append([0])
        path.append([(i - 1) * (m + 1)])
    for j in range(1, m + 1):
        values[0].append(0)
        path[0].append(j - 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
#            print values[i - 1][j], values[i][j - 1], values[i - 1][j - 1] + int(seq1[i] == seq2[j]),i,j,seq1[i],seq2[j]
            max_values = max(values[i - 1][j], values[i][j - 1], values[i - 1][j - 1] + int(seq1[i] == seq2[j]))
            if max_values == values[i - 1][j]:
                path[i].append((m + 1) * (i - 1) + j)
            elif max_values == values[i][j - 1]:
                path[i].append((m + 1) * i + j - 1)
            else:
                path[i].append((m + 1) * (i - 1) + j - 1)
            values[i].append(max_values)
    return (values, path)
    
def BackTrackLCS(path):
    n = len(path) - 1
    m = len(path[0]) - 1
    path_res = [(n, m)]
    pos = (n, m)
    while pos[0] > 0 and pos[1] > 0:
#        print pos
        pos = path[pos[0]][pos[1]]
        pos = (pos / (m + 1), pos % (m + 1))
        path_res.append(pos)
    path_res.reverse()
    return path_res

def ShowAlignment(seq1, seq2, path):
    alignedseq = ''
    old_pos = path[0]
    for pos in path[1:]:
        if pos[0] > old_pos[0] and pos[1] > old_pos[1]:
            alignedseq += seq1[pos[0]-1]
        old_pos = pos
    return alignedseq
    
seq1 = 'AACCTTGG'
seq2 = 'ACACTGTGA'

seq1 = 'GTAGGCTTAAGGTTA'
seq2 = 'TAGATA'
(vals, track) = MahattanTourist(seq1, seq2)
#print path
path =  BackTrackLCS(track)
print path
print ShowAlignment(seq1, seq2, path)