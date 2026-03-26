class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        n=s[::-1]
        m=" ".join(n)
        return m