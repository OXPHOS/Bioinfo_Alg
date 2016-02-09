'''
     Input: A permutation.
     Output: The number of breakpoints in this permutation.
     
Represent the beginning and end of permutation P by adding 0 to the left of the first element 
and n + 1 to the right of the last element: (0 p1 ... pn (n + 1))
(2,3) or (-7,-6) are considered in order. Other neighbors are considered as breakpoints.
'''


def input_permutation(perm):
    'Transform string into int list'
    perm = perm[1 : -1]
    perm_list = perm.split()
    curr_order = [0]
    
    for item in perm_list:
        if item[0] == '-':
            curr_order.append(-int(item[1:]))
        else:
            curr_order.append(int(item[1:]))
    curr_order.append(len(curr_order))
    return curr_order
    
def breakpoint(curr_order):    
    breakpoint = 0
    for i in range(len(curr_order)-1):
        if curr_order[i + 1] - curr_order[i] != 1:
            breakpoint += 1
    print breakpoint
    
perm = '(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)'
curr_order = input_permutation(perm)
breakpoint(curr_order)