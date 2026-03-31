class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        c=""
        v=""
        for ch in word1:
            c+=ch
        for s in word2:
            v+=s
        if c==v:
            return True
        else:
            return False        

               