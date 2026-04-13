class Solution(object):
    def areNumbersAscending(self, s):
        a=[]
        for i in s.split():
            if i.isdigit():
                a.append(int(i))
        return a==sorted(a)  and len(a) == len(set(a)) 