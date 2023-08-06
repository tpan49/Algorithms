import queue

MAX = 1000+5
dist = [0]*MAX
visited = [False]*MAX
graph = [[] for i in range(MAX)]

num_q = int(input())

def BFS(s):
   q = queue.Queue()
   visited[s] = True
   q.put(s) 
   
   while not q.empty():
       u = q.get()
       
       for v in graph[u]:
           if not visited[v]:
               dist[v] = dist[u] + 1
               visited[v] = True
               q.put(v)

for _ in range(num_q):
    V, E = map(int, input().split())
    
    for i in range(MAX):
        visited[i] = False
        graph[i].clear()
        dist[i] = 0
    
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        
    s = int(input())
    BFS(s)
    
    for i in range(1, V+1):
        if i == s:
            continue
        print(dist[i]*6 if visited[i] else -1, end=' ')
        
    print()
    
    