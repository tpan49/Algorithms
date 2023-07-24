# 1st try
# n = int(input())
# left = []
# right = []

# for i in range(n):
#     l,r = map(int, input().split())
#     left.append(l)
#     right.append(r)
    
# minimum = min(left)
# maximum = max(right)

# for i in range(n):
#     if left[i]==minimum and right[i]==maximum:
#         print(i+1)
#         exit()

# print(-1)

#2nd try
n = int(input())
starts = []
ends = []

for i in range(n):
    s, e = map(int, input().split())
    starts.append(s)
    ends.append(e)
    
min = min(starts)
max = max(ends)

for i in range(n):
    if starts[i] == min and ends[i] == max:
        print(i+1)
        exit()
    
print(-1)