class Solution(object):
    def sortArrayByParity(self, nums):
        a=[]
        b=[]
        for i in nums:
            if i%2==0:
                a.append(i)
                a.sort()
            else:
                b.append(i) 
                b.sort()
        return a+b 