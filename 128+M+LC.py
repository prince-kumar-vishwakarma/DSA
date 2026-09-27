# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        longest = 0
        for k,v in hm.items():
            if k-1 in hm:
                continue
            temp = k
            while temp in hm:
                temp += 1
            longest = max(longest, temp-k)
        return longest
        