class Solution(object):
    def lengthOfLastWord(self, s):
       s=s.split()
       for i in s:
            m=s[-1]
            return len(m)  