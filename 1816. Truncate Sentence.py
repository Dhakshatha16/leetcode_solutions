class Solution(object):
    def truncateSentence(self, s, k):
            s=s.split()
            d= s[:k]  
            return " ".join(d)