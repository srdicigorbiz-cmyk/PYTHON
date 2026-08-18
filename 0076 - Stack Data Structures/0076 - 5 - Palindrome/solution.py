from stack import Stack


def isPalindrome(s):
    # Write code here
    stack = Stack()
    
    for l in s:
        stack.push(l)
    
    for l in s:
        if l != stack.pop():
            return False
    
    return True