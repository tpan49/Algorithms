k, money, n = map(int, input().split())
total = 0
for i in range(1, n+1):
    total += i*k
    
print(total-money if total-money>0 else 0)