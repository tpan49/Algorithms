n, m, x, y = map(int, input().split())
a =  list(map(int, input().split()))
b =  list(map(int, input().split()))
ans = []

j=0
for i in range(n):
    if j<m and b[j] >= a[i]-x and b[j] <= a[i]+y:
        ans.append((i+1, j+1))
        j +=1
            
print(len(ans))

for p in ans:
    print(p[0], p[1])


