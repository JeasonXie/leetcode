# coding=gbk
class Solution:
  def twoSum( nums, target):
    dic = dict()
    for index,value in enumerate(nums):#枚举enumerate[index,value]后计入字典。
        sub = target-value
        if sub in dic:#有就找到！没有则记录这个索引，数据。（从这里开始调用dic=dict）
            print(dic[sub],index)
            break
            return [dic[sub],index]

        else:
            dic[value] = index   #记录上面enumerate枚举的值和索引，入字典
            print(dic,index)

nums = [3,4,5,2]    #先纪录一遍，=====================================
print(Solution.twoSum(nums,6))