class Solution(object):
    def getSneakyNumbers(self, nums):
        s=set()
        sn=[]
        for ch in nums:
            if ch not in s:
                s.add(ch)
            else:
                sn.append(ch)
        return sn            
                   