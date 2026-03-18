class Solution(object):
    def checkIfPangram(self, sentence):
        sentence=sentence.lower()
        sentence=set(sentence)
        c=0
        z="abcdefghijklmnopqrstuvwxyz"
        for ch in sentence:
            if ch in z:
                c+=1
        if c==26:
            return True
        else:
           return False  