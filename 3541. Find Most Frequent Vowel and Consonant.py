class Solution(object):
    def maxFreqSum(self, s):
        a = "aeiouAEIOU"
        max_v = 0
        max_c = 0
        for ch in s:
            count = s.count(ch)
            if ch in a:
                if count > max_v:
                    max_v = count
            else:
                if count > max_c:
                    max_c = count
        return max_v + max_c