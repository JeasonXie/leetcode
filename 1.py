# coding=gbk
class Solution:
  def twoSum( nums, target):
    dic = dict()
    for index,value in enumerate(nums):#ö��enumerate[index,value]������ֵ䡣
        sub = target-value
        if sub in dic:#�о��ҵ���û�����¼������������ݡ��������￪ʼ����dic=dict��
            print(dic[sub],index)
            break
            return [dic[sub],index]

        else:
            dic[value] = index   #��¼����enumerateö�ٵ�ֵ�����������ֵ�
            print(dic,index)

nums = [3,4,5,2]    #�ȼ�¼һ�飬=====================================
print(Solution.twoSum(nums,6))