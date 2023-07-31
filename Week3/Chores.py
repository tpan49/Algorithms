n, a, b = map(int, input().split())
l = list(map(int, input().split()))

l = sorted(l, key=lambda x: -x)

ans = l[a-1]-l[a]
print(ans if ans>0 else 0)    