import queue

while(True):
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        exit()
        
    # inf = 10**9
    # dist = [[0] for i in range(C)]
    # graph = [[False] for i in range(C)]
    level = [False] * R
    q = [0] * (R * R)
    
    # for i in range(R):
    #     print(dist[i][i])
    #     print(graph[i][i])
    # print(len(dist))
    # print(len(dist[0][9]))