def input_chr(graph_p):
    'Separate chromosomes into lists'
    graph_chrs = graph_p[1 : -1]
    graph_chrs = graph_chrs.split(')(')
    chrs = []
    for graph_chr in graph_chrs:
        graph_chr_list = graph_chr.split()
        chr = []
        for item in graph_chr_list:
            if item[0] == '-':
                chr.append(-int(item[1:]))
            else:
                chr.append(int(item[1:]))
        chrs.append(chr)
    return chrs

def chr_to_cycle(chromosome):
    'Transform a chromosome Chromosome containing n synteny blocks into int list'
    'Tail: 2k -- > head: 2k + 1'
    'For eg. Input (+1 -2 -3)(+4 +5 -6), output: [1, 2, 4, 3, 6, 5][7, 8, 9, 10, 12, 11]'
    nodes = [[] for _ in range(2 * len(chromosome))]
    for j in range(len(chromosome)):
        i = chromosome[j]
        if i > 0:
            nodes[2 * j] = 2 * i - 1
            nodes[2 * j + 1] = 2 * i
        else:
            nodes[2 * j] = - 2 * i
            nodes[2 * j + 1] = - 2 * i - 1
    return nodes
    
    
def cycle_to_chr(nodes):
    'Transform a Nodes list back into chromosome. length/2'
    'For eg. Input: [(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)], Output: [1, -2, -3][-4, 5, -6]'
    chromosome = [[] for _ in range(len(nodes) / 2)]
    for j in range(len(nodes) / 2):
        if nodes[2 * j] < nodes[2 * j + 1]:
            chromosome[j] = nodes[2 * j + 1] / 2
        else:
            chromosome[j] = - nodes[2 * j] / 2
    return chromosome

def colored_edges(graph_p):
    'Generate list showing the edges in one graph.'
    'Two endpoints of an edge are recorded in a tuple as an element in list'
    'For eg. [(2, 4), (3, 6), (5, 1), (8, 9), (10, 12), (11, 7)]'
    edges = list()
    chrs = input_chr(graph_p)
    for chr in chrs:
        nodes = chr_to_cycle(chr)
        for j in range(len(chr) - 1):
            edges.append((nodes[2 * j + 1], nodes[2 * j + 2]))
        edges.append((nodes[2 * len(chr) - 1], nodes[0]))
    return edges
                   
def graph_to_genome(genome_graph):
    'Reverse: transform graph (lists with tuples) back into genome (1 -2 -3 4) etc.'
    'For eg. [[1, -2, -3], [-4, 5, -6]]'
    genome = []
    index = 0

    while index < len(genome_graph):
        start = genome_graph[index][0]
        if start % 2 == 0:
            end = start - 1
        else:
            end = start + 1
        
        nodes = [end, start]
        for i in range(index, len(genome_graph)):
            if i > index:
                nodes.extend((genome_graph[i - 1][1], genome_graph[i][0]))
            if genome_graph[i][1] == end:
                genome.append(cycle_to_chr(nodes))
                break
        index = i + 1
        
    return genome
            
            
                                       
graph_p = '(+1 -2 -3)(+4 +5 -6)'
print colored_edges(graph_p)
genome_graph = [(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)]
print graph_to_genome(genome_graph)
