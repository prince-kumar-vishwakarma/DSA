# 2965. Find Missing and Repeated Values

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hm = [0]*(n*n)
        a = -1
        for row in grid:
            for e in row:
                hm[e-1] += 1
                if hm[e-1] == 2:
                    a = e

        
        for i,n in enumerate(hm):
            if n == 0:
                return [a, i+1]

        