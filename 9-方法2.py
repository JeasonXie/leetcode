def is_palindrome(n):
    n=str(n)
    m=n[::-1]
    if n==m:
        return True
    else:
        return False
print(is_palindrome(-101))