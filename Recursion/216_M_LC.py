# 216. Combination Sum III

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        if n < ((k*(k+1))//2): return []

        ans = []
        nums = [i for i in range(1,10)]

        def backtrack(idx, n, arr):
            if n == 0 and len(arr) == k: 
                ans.append(arr[:])
                return
            if n<=0 or idx == 9: return 

            arr.append(nums[idx])
            backtrack(idx+1, n-nums[idx], arr)
            arr.pop()
            backtrack(idx+1, n, arr)
        backtrack(0, n, [])
        return ans