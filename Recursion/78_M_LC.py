# 78. Subsets

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        for i in range(2**n):
            cur = []
            for j in range(n):
                if (i & (1<<j)) != 0:
                    cur.append(nums[j])
            ans.append(cur)
        return ans

        