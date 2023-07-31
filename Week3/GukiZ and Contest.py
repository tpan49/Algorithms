n = int(input())
my_list = list(map(int, input().split()))

sorted_list = sorted(my_list, key=lambda x: -x)
rank = [0]*2001

for i in range(n):
    mark = sorted_list[i]
    if not rank[mark]:
        rank[mark] = i+1
        
for grade in my_list:
    print(rank[grade], end =' ')
