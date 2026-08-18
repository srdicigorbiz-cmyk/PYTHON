from stack import Stack


def isBalancedParentheses(s):
    # Write code here
    stack = Stack()

    parenthesis = {
        ")":"(",
        "]":"[",
        "}":"{"
    }
    
    
    for p in s:
        if p in parenthesis.values():
            stack.push(p)
        if p in parenthesis.keys():
            if stack.empty():
                return False
            else:
                if stack.top() == parenthesis[p]:
                    stack.pop()
                else:
                    return False
    
    if stack.empty():
        return True
    else:
        return False
                
