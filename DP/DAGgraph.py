'''
Calculate longest path of a DAG graph

Input: An integer representing the source node of a graph, followed by an integer representing the
     sink node of the graph, followed by a list of edges in the graph. The edge notation 0->1:7 indicates
     that an edge connects node 0 to node 1 with weight 7. 
Output: The length of a longest path in the graph, followed by a longest path.
'''
import re

def GenerateAdjMatrix(input):
    edges_list = []
    nodes_set = set()
    
    # Split lines, take down edge information and total number of nodes
    for line in input.splitlines():
        line = line.strip()
        nums = re.split('->|:', line)
        edges_list.append(nums)
        nodes_set.update(nums[0:2])
    
        
    nodes_list = list(nodes_set)
    nodes_list.sort()
    print 'nodes_list:', nodes_list
    admtx = [[0]*len(nodes_list) for _ in range(len(nodes_list))]
    
    # Generate adjcent matrix according to the index of each node in nodes_list
    for edge in edges_list:
        admtx[nodes_list.index((edge[0]))][nodes_list.index((edge[1]))] = int(edge[2])
    return nodes_list, admtx

def TopoOrder(source, sink, matrix):
    size = len(matrix)
    matrix_copy = list(matrix)
    
    # Initialze topological graph
    nodes_left = range(size)
    nodes_topo = [source]
    nodes_left.remove(source)

    # Remove sourceless nodes
    dummy = True
    while dummy:
        length = len(nodes_left)
        
        for node in nodes_left:
            if sum(matrix_copy[_][node] for _ in range(size)) == 0:
                nodes_left.remove(node)
                matrix_copy[node] = [0] * size
#                print node

        if length == len(nodes_left):
            dummy = False
                
   
    # Construct topological graph
    while nodes_topo[-1] != sink:
        matrix_copy[nodes_topo[-1]] = [0] * size
        for node in nodes_left:
            if sum(matrix_copy[_][node] for _ in range(size)) == 0:
                nodes_topo.append(node)
                nodes_left.remove(node)
#                print 'nodes_topo',nodes_topo
#                print 'nodes_left',nodes_left
                break

    print 'topo graph:', nodes_topo
    return nodes_topo

def LongestPath(matrix, nodes_topo):
    size = len(nodes_topo)
    values = [0] * size
    trace = [0]
    
    # j is current node and i is all precedent nodes of j
    # value saves the maximum value from source to current node (j)
    # trace saves the most recent precedent node (as index of the node in nodes_topo) of j
    for j in nodes_topo[1 : ]:
        j_index = nodes_topo.index(j)
        max_value = -1

        for i in nodes_topo[0 : j_index]:
            i_index = nodes_topo.index(i)
#            print values, i, matrix[i][j], matrix[i][j] + values[i_index]
            if (matrix[i][j] != 0) and (matrix[i][j] + values[i_index] > max_value):
                max_value = matrix[i][j] + values[i_index]
                precedent_node = i_index
        values[j_index] = max_value
        trace.append(precedent_node)        
        # input_nodes = [i for i in nodes_topo[0 : j] if matrix[i][j] != 0]
        # values[j] = max(matrix[i][j] + values[i] for i in input_nodes)
    print 'max value is:', values[-1]
#    print trace
    
    # Transform trace into path
    path = [nodes_topo[-1]]
    while path[-1] != nodes_topo[0]:
        path.append(nodes_topo[trace[nodes_topo.index(path[-1])]])
    path.reverse()
    return path
    
def Output(source, path, node_ref):
    output = source
    for node in path[1 : ]:
        output = output + '->' + str(node_ref[node])
    return output
        

source = '0'
sink = '44'


input = '''6->26:32
10->39:30
26->28:24
3->16:19
10->35:35
10->37:19
10->31:36
10->33:32
10->32:4
15->23:0
15->21:0
22->24:0
22->27:31
1->3:36
5->43:37
8->30:23
19->34:11
12->13:38
39->40:35
12->15:29
27->29:13
1->42:31
24->25:2
1->10:4
4->30:11
13->35:17
24->28:2
23->25:37
31->43:7
31->40:17
3->28:2
5->12:39
5->11:37
3->4:4
2->31:23
14->29:13
19->27:21
27->36:20
31->33:23
30->40:27
28->42:29
21->35:33
21->37:5
20->37:24
2->9:38
0->14:19
4->20:0
1->41:8
8->14:28
19->20:13
4->43:3
14->31:25
14->30:22
13->41:19
13->40:32
14->35:10
10->11:5
14->38:23
2->23:9
2->25:1
24->40:37
12->38:38
20->23:34
20->21:29
12->30:10
12->37:12
29->44:30
33->35:15
33->37:22
0->36:8
37->38:17
10->29:13
17->44:11
6->14:5
10->22:8
22->37:19
22->34:3
32->43:4
15->36:28
11->35:20
2->16:27
7->10:22
11->31:19
16->41:24
15->30:25
32->37:29
0->27:9
0->28:7
32->38:0
12->43:5
22->35:37
24->30:7
24->32:19
24->38:38'''

source = 'a'
sink = 'g'
input = '''a->b:5
a->c:6
a->d:5
b->c:2
b->f:4
c->e:4
c->f:3
c->g:5
d->e:4
d->f:5
e->g:2
f->g:1'''


[nodes_list, admtx] = GenerateAdjMatrix(input)
print nodes_list
nodes_topo = TopoOrder(nodes_list.index(source), nodes_list.index(sink), admtx)
path = LongestPath(admtx,nodes_topo)
print Output(source, path, nodes_list)
