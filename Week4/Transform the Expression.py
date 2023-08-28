
n = int(input())

for i in range(n):
    str = input()
    ans = ""
    
    stack = []
    # stack = stack.clear()
    
    for j in range(len(str)):
        if str[j].isalpha():
            ans += str[j]
        elif str[j] == ')':
            ans +=stack.pop()
            stack.pop()
        else:
            stack.append(str[j])
    print(ans)
    # print(stack)
    