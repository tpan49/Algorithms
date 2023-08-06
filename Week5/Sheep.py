import queue
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

MAX = 501
backyards = [None] * MAX
totalSheep = totalWolf = 0
    
def BFS(ir, ic):
    global totalSheep, totalWolf
    q = queue.Queue()
    q.put((ir, ic))
    
    sheep = (1 if backyards[ir][ic] == 'k' else 0)
    wolf = (1 if backyards[ir][ic] == 'v' else 0)
    
    canEscape = False
    backyards[ir][ic] = '#'
    
    while not q.empty():
        ur, uc = q.get()
        
        for i in range(4):
            r = ur + dr[i]
            c = uc + dc[i]
            
            if not (r in range(N) and c in range(M)):
                canEscape = True
                continue
            
            if backyards[r][c] != '#':
                sheep += (1 if backyards[r][c] == 'k' else 0)
                wolf += (1 if backyards[r][c] == 'v' else 0)
                backyards[r][c] = '#'
                q.put((r, c))
                
    if canEscape:
        totalSheep += sheep
        totalWolf += wolf
    else:
        if sheep > wolf:
            totalSheep += sheep
        else:
            totalWolf += wolf
            
N, M = map(int, input().split())

for i in range(N):
    backyards[i] = list(input())
    
for i in range(N):
    for j in range(M):
        if backyards[i][j] != '#':
            BFS(i,j)

print(totalSheep, totalWolf)