class Solution(object):
    def isIsomorphic(self, s,t):
        a=[]
        b=[]
        for i in s:
            a.append(s.index(i))
        for i in t:
            b.append(t.index(i))
        if a==b:
            return True
        else:
            return False    