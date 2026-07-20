brackets = {'}':'{',']':'[',')':'('}
s = ")(){}"
stack = []
for i in s:

    if i in brackets.values():
        stack.append(i)
        
    elif i in brackets.keys():
       
        if stack and stack[-1] == brackets[i]:
          
            stack.pop()
            
        else:
            stack.append(i)

print(False if stack or len(s)==1 else True)
