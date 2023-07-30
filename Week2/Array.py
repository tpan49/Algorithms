n, k = map(int, input().split())
l = list(map(int, input().split()))

my_list = [0]*(n+10)
count = start = 0
ans = []
length = []

for end in range(n):

    if my_list[l[end]] == 0:
        count += 1
    
    my_list[l[end]] +=1
    
    while count == k:
        ans.append((start+1, end))
    
        if my_list[l[start]] == 1:
            count -= 1
        
        my_list[l[start]] -=1
        start += 1
        
print("here", my_list[l[n-1]])
if my_list[l[n-1]] != 0:
        count += 1
print(count)

if n==1:
    if ans: 
        print(1, 1)
    else:
        print(-1, -1)
elif count<k:
    print(-1, -1)
else:
    differences = [pair[1] - pair[0] for pair in ans]
    index_of_smallest_diff = differences.index(min(differences))
    pair_with_smallest_diff = ans[index_of_smallest_diff]
    print(pair_with_smallest_diff[0], pair_with_smallest_diff[1])

