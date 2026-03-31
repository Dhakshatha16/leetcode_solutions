class Solution(object):
    def searchMatrix(self, matrix, target):
        found=False
        for ch in matrix:
            if target in ch:
                found=True
                break
        return found   