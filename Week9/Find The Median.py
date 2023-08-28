n = int(input())
arr = list(map(int, input().split()))

arr.sort()
size = len(arr)
print(arr[size//2])