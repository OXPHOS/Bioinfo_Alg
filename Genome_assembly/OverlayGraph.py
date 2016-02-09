'''
Overlay Graph and Hamilton Path

Nodes are k kmers (Compared to DeBrujin Graph where Edges are kmers)

Input: A collection Patterns of k-mers.
Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.

for n kmers, if kmer[i][1:k] == kmer[j][0:k-1], an egde point from node i to node j
'''
def input_data(sequences):
    global seq
    seq = []
    for line in sequences.splitlines():
        seq.append(line.strip())
    seq.sort()

def generate_di_graph():
    l = len(seq[0])
    graph = {}
    for i in range(len(seq)):
        key = seq[i]
        graph[key] = {}
        for j in range(len(seq)):
            if i != j and seq[i][1 : l] == seq[j][0 : l - 1]:
                graph.update({key: seq[j]})   # Didn't add multi-items to the key. Just replaced the old item to the key
                break
#        print graph
    return graph

def output(graph):
    for key in seq: # To output key in alphabetic order
        if len(graph[key])!= 0:
            print key, '->', graph[key]

sequences = '''ATGCG
GCATG
CATGC
AGGCA
GGCAT'''

input_data(sequences)
di_graph = generate_di_graph()
output(di_graph)        
        