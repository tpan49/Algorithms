s = list(input())
t = list(input())


for i in range(len(s)-1, -1, -1):
    if s[i] == 'z':
        print("here")
        s[i] = 'a'
    else:
        s[i] = chr(ord(s[i])+1)
        # print(s[i])
        break
     
print(''.join(s) if s!=t else "No such string")
    
