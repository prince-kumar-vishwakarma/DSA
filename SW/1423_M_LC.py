# 1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        l = n-k
        score = 0
        wS = 0
        for i in range(l, n+k):
            wS += cardPoints[i%n]
            if i-l+1 > k:
                wS -= cardPoints[l]
                l += 1
            score = max(score, wS)
        return score
        