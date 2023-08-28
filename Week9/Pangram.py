n = int(input())
string = input()
fre = [0]*26

for i in range(n):
    letter = string[i].lower()
    fre[ord(letter)-97] += 1
    
for i in range(26):
    if fre[i] > 0:
        continue
    else:
        print('NO')
        exit()
print('YES')