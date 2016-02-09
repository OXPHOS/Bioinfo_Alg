'''
     Input: An integer k.
     Output: A k-universal circular string.
'''


import random
########################################################################
###################        Generate all kmers       ####################
########################################################################
def generate_kmer(k):
    kmers = []
    for i in range(2**k):
        kmers.append(format(i, '0' + str(k) + 'b'))
#    print kmers
    return kmers

########################################################################
#################        Generate DeBrujin Graph      ##################
########################################################################    
def kmer_generate_graph(kmers):
    # Add each kmer to dict and merge
    graph = {}
    for kmer in kmers:
        key = kmer[0: -1]
        if key in graph:
            graph[key].append(kmer[1: ])
        else:
            graph[key] = [kmer[1: ]]
#    print graph
    return graph

########################################################################
###########     Find Eulerian Path From DeBrujin Graph     #############
########################################################################

def eulerian_cycle(k):
    
    # Generate graph dict, calculate total edges, initiate available nodes set
    kmers = generate_kmer(k)
    num_edges = len(kmers)
    graph = kmer_generate_graph(kmers)
    #print graph, num_edges
    
    #######################################################################
    # Get start point
    path = []
    stack = []
    start = random.choice(graph.keys())
    current = start
    graph_temp = graph

    while len(path) < num_edges:
        if len(graph_temp[current]) == 0:
            path.append(current)
            current = stack.pop()
        else:
            stack.append(current)
            next = graph_temp[current][0]
            graph_temp[current].remove(next)
            current = next
    #path.append(start)
    return path # This is a reverse path with end node at the first place

########################################################################
##################    Eulerian Path To Sequence     ####################
########################################################################

def path_to_dna(path):
    seq = ''
    for _ in range(0, len(path)):
        seq = path[_][-1] + seq
        
    
    print seq

########################################################################
##########################    Input part     ###########################
########################################################################
path = eulerian_cycle(9) #9
path_to_dna(path)