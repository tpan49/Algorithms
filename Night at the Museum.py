s = input()

if s[0] != 'a':
    s = 'a'+s

res = 0
for i in range(len(s)-1):
    rotate1Value = (ord(s[i]) - ord(s[i+1]))  
    rotate2Value = ord(s[i+1]) - ord(s[i]) 
    rotate1Value = rotate1Value if rotate1Value >= 0 else rotate1Value+26
    rotate2Value = rotate2Value if rotate2Value >= 0 else rotate2Value+26  
    res += rotate1Value if rotate1Value < rotate2Value else rotate2Value
    print("Res: ", res)

     

