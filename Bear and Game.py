# 1st try
# n = int(input())
# v = list(map(int, input().split()))

# def check(n,v):
# 	keepTrack = v[0]
# 	if keepTrack > 15:
# 		return 15
# 	for i in range(n-1):
# 		distance = v[i+1]-v[i]
# 		if distance>15:
# 			return v[i]+15
# 		keepTrack = v[i+1]
# 	return keepTrack+15

# res = check(n,v)
# print(res if res<90 else 90)

#2nd try
n = int(input())
l = list(map(int, input().split()))
key = 15
max=90
size = len(l)

if l[0]>key:
    print(key)
    exit()
else:
    for i in range(size-1):
        diff = l[i+1]-l[i]
        if diff > key:
            print(l[i]+key if l[i]+key<max else max)
            exit()
            
ans = l[size-1]+key
print(ans if ans<max else max)
			