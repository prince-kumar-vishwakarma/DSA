# 506. Relative Ranks
# https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        temp = [-x for x in score]
        heapq.heapify(temp)
        rank = 1
        hm = {}
        while temp:
            if rank == 1:
                hm[-heapq.heappop(temp)] = "Gold Medal"
            elif rank == 2:
                hm[-heapq.heappop(temp)] = "Silver Medal"
            elif rank == 3:
                hm[-heapq.heappop(temp)] = "Bronze Medal"
            else:
                hm[-heapq.heappop(temp)] = f"{rank}"
            rank += 1
        for i,n in enumerate(score):
            score[i] = hm[n]
        return score





        