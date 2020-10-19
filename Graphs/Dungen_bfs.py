# we can move only right , left , top and bottom with cost 1
# Need to find minimum number of steps to get to E

'''
Sample input:

5
7
S . . # . . .
. # . . . # .
. # . . . . .
. . # # . . .
# . # E . # .
Start Row Index: 0
Start Column Index:0

Sample output:
9
'''

def explore_neighbours(r,c,R,C,visited,Grid,x_queue,y_queue):
    cnt = 0
    dr = [-1,1,0,0]
    dc = [0,0,1,-1]
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        if rr >= R or rr < 0:
            continue
        if cc >= C or cc < 0:
            continue

        if visited[rr][cc]:
            continue

        if Grid[rr][cc] == "#":
            continue

        x_queue.append(rr)
        y_queue.append(cc)
        visited[rr][cc] = True
        cnt += 1
    return cnt



def Dungeon(Grid,start_row_index,start_col_index,R,C):
    sr = start_row_index
    sc = start_col_index

    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0

    reached_end = False
    visited = [[False for _ in range(C)] for _ in range(R)]
    x_queue = []
    y_queue = []
    x_queue.append(sr)
    y_queue.append(sc)

    while len(x_queue) != 0:
        r = x_queue.pop(0)
        c = y_queue.pop(0)
        if Grid[r][c] == "E":
            reached_end = True
            break
        nodes_in_next_layer += explore_neighbours(r,c,R,C,visited,Grid,x_queue,y_queue)
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1

    if reached_end:
        return move_count
    else:
        return -1



if __name__ == "__main__":
    R = int(input())
    C = int(input())
    Grid = [[None] for i in range(R)]
    for i in range(R):
        Grid[i] = list(input().split())
    start_row_index = int(input("Start Row Index: "))
    start_col_index = int(input("Start Column Index:"))
    print(Dungeon(Grid,start_row_index,start_col_index,R,C))
