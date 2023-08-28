import queue
tries = int(input())

for _ in range(tries):
    ans = 0
    n, m = map(int, input().split())
    q = queue.Queue()
    l = list(map(int, input().split()))
    my_job = l[m]
    for i in range(n):
        if i == m:
            q.put(-1)
        else:
            q.put(l[i])
    

    l = sorted(l)
    # print("initial" , q.qsize())
    while(q.empty() is not None):
        # print("len", q.qsize())
        # print("q.queue[0]", q.queue[0])
        # print("l[-1]", l[-1])
        if q.queue[0] == -1 and my_job==l[-1]: 
            print(ans+1)
            break
        elif q.queue[0] < l[-1]:
            q.put(q.get())
            
        elif q.queue[0] >= l[-1]:    
            ans +=1
            q.get()
            l.pop()
            
            
    
    
    
    