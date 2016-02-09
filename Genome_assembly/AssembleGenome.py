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
    kmers = []
    for line in Dna.splitlines():
        kmers.append(line.strip())
    
    # Add each kmer to dict and merge
    graph1 = {}
    graph2 = {}
    for kmer in kmers:
        key1 = kmer[0: -1]
        key2 = kmer[1:]
        if key1 in graph1:
            graph1[key1].append(kmer[1: ])
        else:
            graph1[key1] = [kmer[1: ]]
        if key2 in graph2:
            graph2[key2].append(kmer[0:-1])
        else:
            graph2[key2] = [kmer[0:-1]]
#    print graph1
    return (graph1, graph2)

########################################################################
###########     Find Eulerian Path From DeBrujin Graph     #############
########################################################################

def eulerian_path(Dna, k):
    '''
    http://www.dcc.fc.up.pt/~pribeiro/estagio2008/usaco/3_3_EulerianTour.html
    '''
    # Generate graph dict, calculate total edges, initiate available nodes set
    num_edges = len(Dna.splitlines())
    (graph_out, graph_in) = kmer_generate_graph(Dna)
    #print graph, num_edges
    
    #######################################################################
    # Get start point
    start = graph_out.keys()[0]
    for key in graph_out:
        if (not key in graph_in) or (len(graph_out[key]) > len(graph_in[key])): 
            start = key
            break
    path = []
    stack = []
    current = start
    graph_temp = graph_out

    while len(path) < num_edges:
        if (not current in graph_temp) or (len(graph_temp[current]) == 0):
            path.append(current)
            current = stack.pop()
        else:
            stack.append(current)
            next = graph_temp[current][0]
            graph_temp[current].remove(next)
            current = next
    path.append(start)
    return path # This is a reverse path with end node at the first place

########################################################################
##################    Eulerian Path To Sequence     ####################
########################################################################

def path_to_dna(path):
    seq = ''
    for _ in range(0, len(path) - 1):
        seq = path[_][-1] + seq
        
    seq = path[-1] + seq
    print seq

########################################################################
##########################    Input part     ###########################
########################################################################

Dna = '''CTTA
     ACCA
     TACC
     GGCT
     GCTT
     TTAC''' 

path = eulerian_path(Dna, 4)
path_to_dna(path)