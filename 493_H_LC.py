# 493. Reverse Pairs

class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def countPair(nums, l, m, r):
            L = nums[l:m+1]
            R = nums[m+1:r+1]
            i, j = 0,0
            cnt = 0
            while i<len(L) and j<len(R):
                if L[i]>R[j]*2:
                    cnt += len(L)-i
                    j+=1
                else:
                    i += 1
            i, j = 0, 0
            k = l
            while i<len(L) and j<len(R):
                if L[i]<=R[j]:
                    nums[k] = L[i]
                    i+=1
                else:
                    nums[k] = R[j]
                    j+=1
                k+=1
            while i<len(L):
                nums[k] = L[i]
                i+=1
                k+=1
            while j<len(R):
                nums[k] = R[j]
                j+=1
                k+=1
            return cnt

        def breakNums(nums, l, r):
            if l < r:
                mid = (l + r) >> 1
                left = breakNums(nums, l, mid)
                right = breakNums(nums, mid + 1, r)
                pairs = countPair(nums, l, mid, r)
                return left + right + pairs
            return 0
        return breakNums(nums, 0, len(nums)-1)
        