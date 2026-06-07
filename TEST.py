packages = [10, 25, 15, 30, 5, 40]
data1 = list(enumerate(packages))
print(len(data1))
print(data1[1][1])

num=input()
def isPalindrome(num):
    # Write code here
    num = str(num)
    mun = int(num[::-1])
    num = int(num)
    if num == mun:
        return True
    else:
        return False
print(isPalindrome(num))