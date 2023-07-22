n = int(input())
left = []
right = []

for i in range(n):
    l,r = map(int, input().split())
    left.append(l)
    right.append(r)
    
minimum = min(left)
maximum = max(right)

for i in range(n):
    if left[i]==minimum and right[i]==maximum:
        print(i+1)
        exit()

print(-1)