# 40. Combination Sum II


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        def find(idx, target, arr):
            if target == 0: 
                ans.append(arr[:])
                return
            for i in range(idx, n):
                if i>idx and candidates[i] == candidates[i-1]: continue
                if target<candidates[i]: break
                arr.append(candidates[i])
                find(i+1, target-candidates[i], arr)
                arr.pop()
        find(0, target, [])
        return ans


        