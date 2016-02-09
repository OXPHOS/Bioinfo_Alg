'''
Input: A permutation P.
Output: The sequence of permutations corresponding to applying GREEDYSORTING to P, ending with
     the identity permutation.
GREEDYSORTING(P)
    approxReversalDistance <- 0
    for k = 1 to |P|
        if element k is not sorted
            apply the k-sorting reversal to P
            approxReversalDistance <- approxReversalDistance + 1
        if k-th element of P is -k
            apply the k-sorting reversal to P
            approxReversalDistance <- approxReversalDistance + 1
    return approxReversalDistance
'''

def input_permutation(perm):
    'Transform string into int list'
    perm = perm[1 : -1]
    perm_list = perm.split()
    curr_order = []
    for item in perm_list:
        if item[0] == '-':
            curr_order.append(-int(item[1:]))
        else:
            curr_order.append(int(item[1:]))
    
    return curr_order

def output_sorting(steps):
    'Output'
    for step in steps [ 1:]:
        temp_str = '('
        for num in step:
            if num > 0:
                temp_str = temp_str + '+' + str(num) + ' '
            else:
                temp_str = temp_str + str(num) + ' '
        temp_str = temp_str[ : -1] + ')'
        print temp_str
        

def greedy_sorting(perm):
    'Input origin sequence'
    curr_order = input_permutation(perm)
    steps = [curr_order]
    counter = 1
    t = 0
    
    'Sort from 1 to the end'
    while counter <= len(curr_order):
        try:
            index = curr_order.index(counter)
        except ValueError:
            index = curr_order.index(-counter)
            
        'Reverse'
        if index != counter - 1:
            temp_rev = curr_order [counter - 1 : index + 1]
            temp_rev.reverse()
            temp_rev = [-temp_rev[_] for _ in range(len(temp_rev))]
            curr_order [counter - 1 : index + 1] = temp_rev
            steps.append(list(curr_order))
            t += 1
        
        if curr_order[counter - 1] < 0:
            curr_order[counter - 1] = - curr_order[counter - 1]
            steps.append(list(curr_order))
            t += 1
        
        counter += 1
    
    print t
    output_sorting(steps)


perm = '(-3 +4 +1 +5 -2)'
perm = '(+6 -12 -9 +17 +18 -4 +5 -3 +11 +19 +14 +10 +8 +15 -13 +20 +2 +7 -16 -1)'
greedy_sorting(perm)