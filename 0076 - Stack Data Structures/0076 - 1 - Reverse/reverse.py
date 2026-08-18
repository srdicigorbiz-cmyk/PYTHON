from stack import Stack


def reverse(a):
    # Write code here
    stack = Stack()
    result = []
    for n in a:
        stack.push(n)
    
    while not stack.empty():
        result.append(stack.pop())
        
    return result