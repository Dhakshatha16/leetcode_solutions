class Solution(object):
    def removeDuplicates(self, nums):
        new = []
        for i in nums:
            if i not in new:
                new.append(i)
                
        nums[:] = new
        return len(nums) 