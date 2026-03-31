class Solution(object):
    def reversePrefix(self, word, t):
        if t in word:
            i = word.index(t)
            return word[:i+1][::-1] + word[i+1:] 
        return word  