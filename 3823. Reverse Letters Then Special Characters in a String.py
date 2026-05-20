class Solution(object):
    def reverseByType(self, s):
        letters = []
        specials = []
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                specials.append(ch)
        result = []
        for ch in s:
            if ch.isalpha():
                result.append(letters.pop())
            else:
                result.append(specials.pop())

        return "".join(result)