n, k = map(int, input().split())
l = list(map(int, input().split()))

my_list = [0]*(n+1)
count = start = 0
ans = 0

for end in range(n):
    while count == k:
        # if my_list[l[start]] == 1:
        #     count -= 1
        if my_list[l[start]] > 1:
            my_list[l[start]] -=1
            start += 1
        print(start+1, end)
        exit()
        
    if my_list[l[end]] == 0:
        count += 1
    my_list[l[end]] +=1
    
    
if count<k:
    print(-1, -1)
    