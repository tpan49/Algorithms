n = int(input())
l = list(map(int, input().split()))
my_list = [0]*100001

start = end = count = ans = 0

while(end<n):
    if my_list[l[end]] == 0:
        count += 1
    my_list[l[end]] += 1
    
    while(count>2 and start<n):
        if my_list[l[start]] == 1:
            count -=1
        my_list[l[start]] -= 1
        start += 1
        
    ans = max(ans, end-start+1)
    end +=1
print(ans)