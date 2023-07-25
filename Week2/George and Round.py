n, m = map(int, input().split())
required = list(map(int, input().split()))
prepared = list(map(int, input().split()))

count = 0
j = 0
for i in range(m):

    if j<n and prepared[i] >= required[j]: 
        count +=1
        j +=1

print(n-count)
