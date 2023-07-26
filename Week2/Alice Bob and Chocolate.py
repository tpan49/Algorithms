n = int(input())
l = list(map(int, input().split()))

aTime = bTime = i= 0
j = n-1
while i<=j:
    if aTime+l[i] <= bTime+l[j]:
        aTime += l[i]
        i+=1
    else:
        bTime += l[j]
        j-=1
        
print(i,n-i)