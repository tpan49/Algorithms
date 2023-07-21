n = int(input())
v = list(map(int, input().split()))

def check(n,v):
	keepTrack = v[0]
	if keepTrack > 15:
		return 15
	for i in range(n-1):
		distance = v[i+1]-v[i]
		if distance>15:
			return v[i]+15
		keepTrack = v[i+1]
	return keepTrack+15

res = check(n,v)
print(res if res<90 else 90)
