# 1st try
# import math

# n, k = map(int, input().split())
# l = [0]*101
# for i in range(n):
#     value = input()
#     # l.append(value)
#     l[len(value)] +=1
    
# password = input()

# best = worst = count = 0
# for i in range(len(password)):
#     best += l[i]
        
# worst = best + l[len(password)] - 1

# best += math.floor(best/k) *5
# worst += math.floor(worst/k) *5

# print(best+1, worst+1)

# 2nd try 
n, k = map(int, input().split())
tries = [0]*101

for i in range(n):
    value = input()
    tries[len(value)] +=1
    
password = input()
count = 0

for i in range(len(password)):
    count += tries[i]
    
count2 = count+tries[len(password)]-1

best = (count//k)*5+count+1
worst = (count2//k)*5+count2+1 
    
print(best, worst)





