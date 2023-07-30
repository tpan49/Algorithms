n, m, x, y = map(int, input().split())
a =  list(map(int, input().split()))
b =  list(map(int, input().split()))
ans = []

i=0
for j in range(m):
    
    while i<n and b[j] > a[i]+y:
        i+=1
        
    if i == n:
        break

    if b[j] >= a[i]-x and b[j] <= a[i]+y:
        ans.append((i+1, j+1))
        i+=1
            
print(len(ans))

for p in ans:
    print(p[0], p[1])

    


