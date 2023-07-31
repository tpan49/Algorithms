n = int(input())
my_list = list(map(int, input().split()))
sorted_list = sorted(my_list)
fre = [0]*1001
highest = -1
count = 0
for i in range(n):
    fre[sorted_list[i]] +=1
    
for i in range(n):
    print(fre[sorted_list[i]])
    if fre[sorted_list[i]] != 0:
        count +=1
    highest = max(highest, fre[sorted_list[i]])
    
print(highest, count)
