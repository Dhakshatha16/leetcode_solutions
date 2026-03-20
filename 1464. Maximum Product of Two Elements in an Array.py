class Solution(object):
    def maxProduct(self, nums):
        a=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                n=(nums[i]-1)*(nums[j]-1)
                a.append(n)
        return max(a) 