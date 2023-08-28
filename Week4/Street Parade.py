while True:
    n = int(input())
    if n == 0:
        break
    l = list(map(int, input().split()))
    stack = []
    location = 1
    i = 0
    
    while i<n:
        if l[i] != location:
            if stack and l[i] > stack[-1]:
                break
            else:
                stack.append(l[i])
                i+=1
        elif stack[-1] == location:
            stack.pop() 
            location += 1 
               
        elif l[i] == location:
            location += 1
            i+=1
            
        
    
    
         
    
            