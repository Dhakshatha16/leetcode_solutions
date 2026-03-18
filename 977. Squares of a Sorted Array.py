class Solution(object):
    def sortedSquares(self, nums):
        a=[]
        for i in nums:
            c=i*i
            a.append(c)
        return sorted(a)