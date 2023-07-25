n = int(input())
l = list(map(int, input().split()))

s_total = d_total = 0
turn = 0
for i in range(n):
    if l[0] >= l[len(l)-1]:
        if turn%2 == 0:
            s_total += l.pop(0)
        else:
            d_total += l.pop(0)
    else:
        if turn%2 == 0:
            s_total += l.pop()
        else:
            d_total += l.pop()
    turn +=1
            
print(s_total, d_total)
        