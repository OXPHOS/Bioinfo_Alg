def Down_text_List(text, n):
    '''
    Generate the list of value of each edge
    '''
    temp_list = [[0 for _ in range(n + 1)]]
    for line in text.splitlines():
        line = line.strip()
        temp_list.append([])
        for value in line.split():
            temp_list[-1].append(int(value))
    return temp_list

def Right_text_List(text):
    '''
    Generate the list of value of each edge
    '''
    temp_list = []
    for line in text.splitlines():
        line = line.strip()
        temp_list.append([0])
        for value in line.split():
            temp_list[-1].append(int(value))
    return temp_list


def MahattanTourist(n, m, Down, Right):
    '''
    Dynamic programing
    n, m : the grid of the final node is [n, m]
    '''
    path = [[]]
    path[0].append(0)
    for i in range(1, n + 1):
        path.append([path[i - 1][0] + Down[i][0]])
    for j in range(1, m + 1):
        path[0].append(path[0][j - 1] + Right[0][j])
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            max_path = max(path[i - 1][j] + Down[i][j], path[i][j - 1] + Right[i][j])
            path[i].append(max_path)
    return path[n][m]


n = 4
m = 4
Down_text = '''1 0 2 4 3
     4 6 5 2 1
     4 4 5 2 1
     5 6 8 5 3
'''
Right_text = '''3 2 4 0
     3 2 4 2
     0 7 3 3
     3 3 0 2
     1 3 2 2
'''
Down = Down_text_List(Down_text, n)
#print Down
Right =  Right_text_List(Right_text)
#print Right

print MahattanTourist(n, m, Down, Right)
                    