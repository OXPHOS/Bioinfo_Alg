'''
DeBrujin Graph for Eulerian Path generation
Edges are kmers, and nodes are k-1 mers (Compared to overlay graphs where nodes are kmers)

Input: a text string or a group of kmers

Output: DeBrujin Graph Adjacent List

'''


def text_generate_graph(seq, k):
    key_list = []
    graph = {}
    for i in range(len(seq) - k + 1):
        key = seq[i : i + k - 1] 
        if key in graph:
            graph[key].append(seq[i + 1: i + k])
        else:
            key_list.append(key)
            graph[key] = [seq[i + 1: i + k]]
    
    output_digraph(graph,key_list) 
    return graph

def kmer_generate_graph(Dna):
    # Read kmers into string list
    kmers = []
    for line in Dna.splitlines():
        kmers.append(line.strip())
    
    # Add each kmer to dict and merge
    key_list = []
    graph = {}
    for kmer in kmers:
        key = kmer[0: -1]
        if key in graph:
            graph[key].append(kmer[1: ])
        else:
            key_list.append(key)
            graph[key] = [kmer[1: ]]
    output_digraph(graph,key_list) 
    return graph
        
    
def output_digraph(graph, key_list):
    key_list.sort()
    for key in key_list:
        i = 0
        print key, '->',
        for item in graph[key]:
            if i == 0:
                print item,
            else:
                print ',', item,
            i += 1
        print 
        
#digraph = text_generate_graph('AAGATTCTCTAAGA', 4)
Dna = '''GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG'''
digraph = kmer_generate_graph(Dna)