# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def find(idx, target, arr, ans):
            if target == 0:
                ans.append(arr[:])
                return
            if target<0 or idx==len(candidates): return

            arr.append(candidates[idx])
            find(idx, target-candidates[idx], arr, ans)
            arr.pop()
            find(idx+1, target, arr, ans)
        ans = []
        find(0, target, [], ans)
        return ans

