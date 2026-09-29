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
        #----------- another sol--------
        def sub(inp, out, ans):
            if not inp:
                return ans.append(out[:])
            out.append(inp[0])
            inp = inp[1:]
            sub(inp, out, ans)
            out.pop()
            sub(inp, out, ans)
        ans = []
        sub(nums, [], ans)
        return ans