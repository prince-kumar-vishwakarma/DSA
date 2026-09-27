# 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans = []
        for i in range(rowIndex+1):
            row = [1]*(i+1)
            for j in range(1, i):
                row[j] = ans[j-1]+ans[j]
            ans = row
        return ans
