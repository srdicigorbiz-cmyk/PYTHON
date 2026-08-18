from stack import Stack


def nse(a):
    # Write code here
    stack = Stack()
    result = []
    
    for element in a:
        while not stack.empty() and stack.top() >= element:    
            stack.pop()
    
        if stack.empty():
            result.append(-1)
            stack.push(element)
        elif stack.top() < element:
            result.append(stack.top())
            stack.push(element)

    return result