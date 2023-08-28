string = input()
ans = 1
for i in range(len(string)):
    if ord(string[i])-97 < 0:
        ans +=1

print(ans)