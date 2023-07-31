n, x = map(int, input().split())
l = list(map(int, input().split()))

l = sorted(l)
ans = 0
for i in range(n):
    x = 1 if x<1 else x
    ans += l[i]*x
    x -= 1
    
print(ans)