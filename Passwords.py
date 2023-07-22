import math

n, k = map(int, input().split())
l = [0]*101
for i in range(n):
    value = input()
    # l.append(value)
    l[len(value)] +=1
    
password = input()

best = worst = count = 0
for i in range(len(password)):
    best += l[i]
        
worst = best + l[len(password)] - 1

best += math.floor(best/k) *5
worst += math.floor(worst/k) *5

print(best+1, worst+1)

