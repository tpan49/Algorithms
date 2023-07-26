n, t = map(int, input().split())
a = list(map(int, input().split()))

count = start = end = ans = 0
while(end<n):
    while(t<a[end]):
        t+=a[start]
        count -=1
        start +=1
    t -= a[end]
    count += 1
    ans = max(ans, count)
    end +=1
print(ans)