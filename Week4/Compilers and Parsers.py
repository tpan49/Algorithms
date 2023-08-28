n = int(input())
l = []
for _ in range(n):
    str = input()
    stack = []
    count = 0
    for i in range(len(str)):
        if str[i] == '<':
            stack.append(str[i])
        else:
            if len(stack) == 0:
                break
            else:
                stack.pop()    
                count += 1
    
    if len(stack) > 0:
        count = 0
    print(count*2)

