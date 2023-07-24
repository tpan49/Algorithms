# 1st try
# s = input()

# if s[0] != 'a':
#     s = 'a'+s

# res = 0
# for i in range(len(s)-1):
#     rotate1Value = (ord(s[i]) - ord(s[i+1]))  
#     rotate2Value = ord(s[i+1]) - ord(s[i]) 
#     rotate1Value = rotate1Value if rotate1Value >= 0 else rotate1Value+26
#     rotate2Value = rotate2Value if rotate2Value >= 0 else rotate2Value+26  
#     res += rotate1Value if rotate1Value < rotate2Value else rotate2Value
#     print("Res: ", res)

#2nd try
s = input()
ans = 0

if s[0] != 'a':
    s = 'a'+s
    
for i in range(len(s)-1):
    value1 = ord(s[i])-ord(s[i+1])
    value2 = ord(s[i+1])-ord(s[i])

    value1 = value1 if value1 >= 0 else value1+26
    value2 = value2 if value2 >= 0 else value2+26
    
    ans += min(value1, value2)  
    
    
print(ans)
    

