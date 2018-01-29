class Solution:
 def isPalindrome(self, x):
   a = 1
   m = 1
   n = 0
   if x<0:
      return False
   b = []
   x1 = x
   flag = True
   while x1>0:
              j = x1%10
              n = n * 10
              n = n+j
              x1  = int(x1/10)
   if n==x :
          flag = True
          print(n)
          return flag
   else:
      flag = False
   return flag

print(Solution.isPalindrome(Solution, 10))