'''
Solve the Eularian path problem
     Input: The adjacency list of an Eulerian directed graph.
     Output: An Eulerian cycle in this graph.
     
Randomly pick a point to start.
If there're still unexplored edges where there's no available way at current node,
we will select a node from the existed path, which still has unexplored edges
then, start from this point, go through the existed path again, and move on to new edges
'''

import random

def input_to_graph(string):
    '''
    From strings to dict
    '''
    num_edges = 0
    graph = {}
    
    for line in string.splitlines():
        line = line.split() # Remove all spaces
        if len(line) != 0: 
            key = int(line[0]) # 1st: key. 2nd: ->. 
            graph[key] = map(int, line[2].split(','))
            num_edges += (len(graph[key]))
    return graph, num_edges    
    
def output_path(path):
    
    output = str(path[0])
    for _ in range(1, len(path)):
        output = output +  '->' + str(path[_])
    print output


def eulerian_path(string):
    '''
    Randomly pick a point to start.
    If there're still unexplored edges where there's no available way at current node,
    We will select a node from the existed path, which still has unexplored edges
    Then, start from this point, go through the existed path again, and move on to new edges
    '''
    # Generate graph dict, calculate total edges, initiate available nodes set
    graph, num_edges = input_to_graph(string)
    
    #######################################################################
    # Get information about start and end nodes
    head_list = [0] * (len(graph) * 2)
    tail_list = [0] * (len(graph) * 2)
    for key in graph:
        head_list[key] += 1 * len(graph[key])
        for _ in range(len(graph[key])):
            tail_list[graph[key][_]] += 1
    counter = 0
    for i in range(len(head_list)):
        if head_list[i] > tail_list[i]:
            start_node = i
            counter += 1
        elif head_list[i] < tail_list[i]:
            end_node = i
            counter += 1
        
        if counter == 2:
            break
        
    #######################################################################   
    # Initiate path, current node, available list
    path = [start_node]
    current = start_node
    if head_list[start_node] > 1:
        available_nodes = set([start_node])
    else:
        available_nodes = set()
    
    if head_list[end_node] == 0:
        graph[end_node] = [start_node]
    else:
        graph[end_node].append(start_node)
    num_edges += 1

    graph_temp = graph
    
    #######################################################################  
    # Iterate
    # 1). No available edges -->finish or startover
    # 2). Only one available edge --> go and remove the current node
    # 3). More than one available edge  --> randomly pick one way and take down this node
    while True:
#        print graph_temp[current]
        if len(graph_temp[current]) == 0:
            if num_edges == 0:
                break
            elif num_edges < 0:
                print 'ERROR!'
                break
            else:
#                print available_nodes
                new_start = random.choice(list(available_nodes))
                index = path.index(new_start)
                path = path[index : -1] + path[0 : index] + [new_start]
                current  = new_start
#                print '--start over-- \n', path    
                                   
        elif len(graph_temp[current]) == 1:
            available_nodes.discard(current) ###Remove this node if it is in the set, because there's no more available edges
            num_edges -= 1
            next = graph_temp[current].pop()
            path.append(next)
            current = next
#            print current, available_nodes
#            print 'busy node', path
        
        else:
            available_nodes.add(current)
            num_edges -= 1
            next = graph_temp[current].pop(random.randrange(len(graph_temp[current])))
            path.append(next)
            current = next
#            print available_nodes
#            print path
     
    #######################################################################
    # Find the start point and end point  
    for i in range(len(path)):
        if path[i] == end_node and path[i + 1] == start_node:
            path = path[i + 1 : ] + path[1 : i + 1]
            break
           
    output_path(path)

string = '''0 -> 2,4
     1 -> 3,0
     2 -> 1
     3 -> 0,4
     4 -> 1
     6 -> 3,7
     7 -> 8
     8 -> 9
     9 -> 6
     '''     
eulerian_path(string)
