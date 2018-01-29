# coding=gbk
class Solution:
   def longestCommonPrefix(self, strs):
       if len(strs)==0:
           return ""
       small = len(strs[0])
       for s in strs:
           if small>len(s):
               small = len(s)
       i = 0
       N = False
       while  i<small:#每个字符串的字符
           j = 1              #j==1为第二个字符串
           ch = strs[0][i]    #赋值第一个字符串，第一个字符，比较的时候最长不能超过samll
           while j<len(strs):   #字符串个数，从j第二个开始
               if strs[j][i]!=ch:  #不等就结束
                   N=True
                   break
               else:     #等于就继续比较下一个字符串，j++
                 j += 1
           if N==True:
                break
           else:
              i +=1
       return strs[0][:i]
w = Solution()
str = ['abffdd','abc','abdeefrwf']
print (w.longestCommonPrefix(str))



