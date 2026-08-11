a = int(input())
b = int(input())

palindromes = [n for n in range(a,b+1) if str(n)==str(n)[::-1]]

if len(palindromes) > 0:
    print(f"Smallest: {min(palindromes)}\nLargest: {max(palindromes)}")
else:
    print("No palindromes found")