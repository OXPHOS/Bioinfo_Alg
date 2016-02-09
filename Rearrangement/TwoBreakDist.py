'''
CODE CHALLENGE: Solve the 2-Break Distance Problem.
Input: Genomes P and Q.
Output: The 2-break distance d(P, Q).

Calcaulte the cycle number in BreakPointGraph(P, Q)
Blocks(P, Q) - Cycle#(P, Q) = 2-break distance
'''


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
                   

def two_break_dist(graph_p, graph_q):
    # Transform gaph (+1 -2 +3) into edges((2, 4) (3, 5) (6, 1))
    edges_p = colored_edges(graph_p)
    edges_q = colored_edges(graph_q)
    
    # Generate non-directional adjacent list from both edges 
    adjlist = [[] for _ in range(2 * len(edges_p) + 1)]
    for i in range(len(edges_p)):
        adjlist[edges_p[i][0]].append(edges_p[i][1])
        adjlist[edges_p[i][1]].append(edges_p[i][0])
    
    for i in range(len(edges_q)):
        adjlist[edges_q[i][0]].append(edges_q[i][1])
        adjlist[edges_q[i][1]].append(edges_q[i][0])
    print adjlist
    
    # Calculate cycle number from red-blue heterous cycles
    adj_copy = list(adjlist)
    cycle = 0
    step = 1 
    j = 0
    while True:
#        print cycle, step, adj_copy
        j += 1
        if adj_copy[step][0] != 0:
            temp_step = adj_copy[step][0]
            adj_copy[step][0] = 0
#            print 'temp_step=',temp_step
            if adj_copy[temp_step][0] == step:
                adj_copy[temp_step][0] = 0
            else:
                adj_copy[temp_step][1] = 0
            step = temp_step
        elif adj_copy[step][1] != 0:
            temp_step = adj_copy[step][1]
            adj_copy[step][1] = 0
            if adj_copy[temp_step][0] == step:
                adj_copy[temp_step][0] = 0
            else:
                adj_copy[temp_step][1] = 0
            step = temp_step
        else:
            cycle += 1
            step = 0
            for i in range(1, len(adj_copy)):
                if adj_copy[i][0] != 0:
                    step = adj_copy[i][0]
                elif adj_copy[i][0] != 0:
                    step = adj_copy[i][1]
            if step == 0:
                break
    print len(edges_p), cycle, len(edges_p)- cycle

            
graph_p = '(+1 +2 +3 +4 +5 +6)'
graph_q = '(+1 -3 -6 -5)(+2 -4)'
two_break_dist(graph_p, graph_q)
