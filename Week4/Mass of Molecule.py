str = input()

def mass(str):
    return 1 if str=='H' else 12 if str=='C' else 16

ans = 0
stack = []
for i in range(len(str)):
    if str[i].isalpha():
        stack.append(mass(str[i]))   
    elif str[i] == '(':
        stack.append(-1)
    elif str[i] == ')':
        sum = 0      
        while stack[-1] != -1:
            sum += stack.pop()
        stack.pop()
        stack.append(sum)
    else:
        multiplication = stack.pop()*int(str[i])
        stack.append(multiplication)

for item in stack:
    ans += item

print(ans)
    