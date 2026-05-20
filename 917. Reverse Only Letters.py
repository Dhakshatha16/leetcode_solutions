class Solution(object):
    def reverseOnlyLetters(self, s):
        l=[]
        for i in s:
            if i.isalpha():
                l.append(i)   
        r=[]
        for i in s:
            if i.isalpha():
                r.append(l.pop())  
            else:
                r.append(i)     
        return "".join(r)                
                
                
            