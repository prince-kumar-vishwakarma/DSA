# 135. Candy

class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        left = [0]*n
        right = [0]*n
        candy = 1
        left[0] = 1
        for i in range(1, n):
            if ratings[i-1]<ratings[i]:
                candy += 1
                left[i] = candy
            else:
                candy = 1
                left[i] = candy
        right[n-1] = 1
        for i in range(n-2, -1, -1):
            if ratings[i+1]<ratings[i]:
                candy += 1
                right[i] = candy
            else:
                candy = 1
                right[i] = candy
        ans = 0
        for i in range(n):
            ans += max(left[i], right[i])
        return ans
