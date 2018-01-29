class Solution:
    def reverse(self, x):
            a = 1
            m = 1
            n = 0
            if x < 0:
                a = -1
                x = x * a
            while x>0:
              m = m*10
              j = x%10
              n = n * 10
              n = n+j
              x  = int(x/10)
            if -2147483648< n*a < 2147483647:
                return n*a
            else:
                return 0
print(Solution.reverse(Solution,-2147483412))