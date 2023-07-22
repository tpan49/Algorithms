n = int(input())
l = list(map(int, input().split()))

size = len(l)
count = 0
if size == 1:
    if l[0] == 1:
        count +=1
else:
    for i in range(size):
        if l[i] == 0:
            count += 1
          
print("YES" if count==1 else "NO")  