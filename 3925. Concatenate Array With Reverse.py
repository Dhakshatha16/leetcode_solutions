class Solution(object):
    def concatWithReverse(self, nums):
        a=[]
        for i in range(len(nums)-1,-1,-1):
            a.append(nums[i])
        return nums+a   