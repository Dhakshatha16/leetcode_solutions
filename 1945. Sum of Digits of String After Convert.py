class Solution(object):
    def getLucky(self, s, k):
        a = []
        b = "abcdefghijklmnopqrstuvwxyz"
        for ch in s:
            a.append(str(b.index(ch) + 1))       
        num = "".join(a)
        for _ in range(k):
            total = 0
            for ch in num:
                total += int(ch)
            num = str(total)
        
        return int(num)     
            