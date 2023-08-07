import queue
MAX = 251
table = [None] * MAX
slick = [0] * (MAX * MAX)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def BFS(i,j):
    q = queue.Queue()
    q.put((i,j))
    table[i][j] = '0'
    count = 1
    
    while not q.empty():
        ur, uc = q.get()
        
        for k in range(4):
            r = dr[k] + ur
            c = dc[k] + uc
            
            if r in range(N) and c in range(M) and table[r][c] == '1':
                table[r][c] = '0'
                q.put((r,c))
                count += 1
                
    slick[count] += 1
        

while True:
    N, M = map(int, input().split())
    
    if N==0 and M==0:
        break
    
    for i in range(N):
        table[i] = input().split()
        for j in range(M):
            slick[i*M+j+1] = 0
            
    nslicks = 0 
    
    for i in range(N):
        for j in range(M):
            if table[i][j] == '1':
                nslicks += 1
                BFS(i,j)
                
    print(nslicks)
    
    for i in range(1, N*M+1):
        if slick[i]:
            print(i, slick[i], sep= ' ')
    
    