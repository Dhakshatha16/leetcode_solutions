class Solution(object):
    def maximumWealth(self, accounts):
        res=[]
        for i in accounts:
            a=0
            for j in i:
                a+=j
                res.append(a)
        return max(res)  