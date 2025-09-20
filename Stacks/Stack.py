stack = []


stack.append('L')
stack.append('I')
stack.append('F')
stack.append('O')
print("Stack: ", stack)

#pop
element=stack.pop()
print(element)
#peek
peek=stack[-1]
print(peek)
#push
add=stack.append('O')
print(stack)
#isEmpty
empty=not bool(stack)
print(empty)

