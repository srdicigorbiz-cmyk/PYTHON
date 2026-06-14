def isPalindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0]==s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False

s = "ABBA"
print(isPalindrome(s))
s = "123456"
print(isPalindrome(s))