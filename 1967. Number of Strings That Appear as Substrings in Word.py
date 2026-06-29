class Solution(object):
    def numOfStrings(self, p, word):
        c=0
        for ch in p:
            if ch in word:
                c+=1
        return c    
