class Solution:
 def isPalindrome(self, x):
   a = 1
   n = 0
   if x<0:
    return False
   b = []
   flag = True
   while x > 0:
       j = x % 10
       b.append(j)
       n = n * 10
       n = n + j
       x = int(x / 10)
   for i in range(len(b)):
        if b[i] != b[len(b) - i - 1]:
            flag = False
   return flag
w =Solution()
print(Solution.isPalindrome(Solution,101))