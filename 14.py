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
       while  i<small:#ÿ���ַ������ַ�
           j = 1              #j==1Ϊ�ڶ����ַ���
           ch = strs[0][i]    #��ֵ��һ���ַ�������һ���ַ����Ƚϵ�ʱ������ܳ���samll
           while j<len(strs):   #�ַ�����������j�ڶ�����ʼ
               if strs[j][i]!=ch:  #���Ⱦͽ���
                   N=True
                   break
               else:     #���ھͼ����Ƚ���һ���ַ�����j++
                 j += 1
           if N==True:
                break
           else:
              i +=1
       return strs[0][:i]
w = Solution()
str = ['abffdd','abc','abdeefrwf']
print (w.longestCommonPrefix(str))



