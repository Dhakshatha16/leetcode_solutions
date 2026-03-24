class Solution(object):
    def convertToTitle(self, columnNumber):
        r=[]
        while columnNumber>0:
            columnNumber-=1
            r.append(chr(columnNumber%26+ord('A')))
            columnNumber//=26
        return ''.join(reversed(r))