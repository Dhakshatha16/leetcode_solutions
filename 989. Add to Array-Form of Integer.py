class Solution(object):
    def addToArrayForm(self, num, k):
        res=int("".join(map(str,num)))
        a=res+k
        s=list(map(int,str(a)))
        return s