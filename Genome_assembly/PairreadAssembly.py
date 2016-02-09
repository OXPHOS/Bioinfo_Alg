'''
Given a list of kmers (sequenced result), assemble the sequence into a single string
Convert the list of kmers into DeBrujin graph (in-degree and out-degree at the same time to identify start node)
Find Eulerian Path with the following method: http://www.dcc.fc.up.pt/~pribeiro/estagio2008/usaco/3_3_EulerianTour.html
********************BEST EULERIAN PATH SOLUTION***********************

'''

########################################################################
#############     Convert seq data to DeBruijin Graph     ##############
########################################################################
def kmer_generate_graph(Dna):
    # Read kmers into string list
    global K, D
    kmers = []
    for line in Dna.splitlines():
        kmers.append(line.strip())
    
    # Add each kmer to dict and merge
    graph1 = {}
    graph2 = {}
    for kmer in kmers:
        key1 = kmer[0 : K - 1] + kmer[K : -1]
        key2 = kmer[1 : K + 1] + kmer[K + 2 : ]
        if kmer == 'GAAAGGTACAAATACTGGCGACCTCGCTGTTCGACACTTCATCACTGCTC|CACGCATACGCTGCACAAGGGACCCTGCTCACTCGATTGGGAATCTAATG':
            print key1, key2
        if key1 in graph1:
            graph1[key1].append(key2)
        else:
            graph1[key1] = [key2]
        if key2 in graph2:
            graph2[key2].append(key1)
        else:
            graph2[key2] = [key1]
#    print len(graph1)
    return (graph1, graph2)

########################################################################
###########     Find Eulerian Path From DeBrujin Graph     #############
########################################################################

def eulerian_path(Dna):
    '''
    http://www.dcc.fc.up.pt/~pribeiro/estagio2008/usaco/3_3_EulerianTour.html
    '''
    # Generate graph dict, calculate total edges, initiate available nodes set
    num_edges = len(Dna.splitlines())
    (graph_out, graph_in) = kmer_generate_graph(Dna)
    start = 'GAAAGGTACAAATACTGGCGACCTCGCTGTTCGACACTTCATCACTGCT|CACGCATACGCTGCACAAGGGACCCTGCTCACTCGATTGGGAATCTAAT'

#    print len(graph_out[start])#, len(graph_in[start])
    
    #######################################################################
    # Get start point
    start = graph_out.keys()[0]
    for key in graph_out:
        if (not key in graph_in) or (len(graph_out[key]) > len(graph_in[key])): 
            start = key
            break
#    print 'start=',start
    path = []
    stack = []
    current = start
    graph_temp = graph_out

    while len(path) < num_edges:
#        print len(path), len(stack)
        if (not current in graph_temp) or (len(graph_temp[current]) == 0):
    
            path.append(current)
            current = stack.pop()
        else:
#            print current,len(current),graph_out[current]
            stack.append(current)
            next = graph_temp[current][0]
            graph_temp[current].remove(next)
            current = next
    path.append(start)
    print num_edges, len(path)
    return path # This is a reverse path with end node at the first place

########################################################################
##################    Eulerian Path To Sequence     ####################
########################################################################

def path_to_dna(path):
    # Very complicated
    
    seq = ''
    for _ in range(0, len(path) - 1):
        seq = path[_][-1] + seq
    
    seq = path[-1][K + 1 : ] + seq
    
    for i in range(D + 2):
        seq = path[i - D - K - 1][0] + seq
    
    seq = path[-1][0 : K - 1] + seq
    print seq

########################################################################
##########################    Input part     ###########################
########################################################################
K = 4
D = 2
# D might be larger than K in some circumstances
Dna = '''GAGA|TTGA
TCGT|GATG
CGTG|ATGT
TGGT|TGAG
GTGA|TGTT
GTGG|GTGA
TGAG|GTTG
GGTC|GAGA
GTCG|AGAT''' 

path = eulerian_path(Dna)
path_to_dna(path)