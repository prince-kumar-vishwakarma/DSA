# 575. Distribute Candies


class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        hm = {}
        for candy in candyType:
            hm[candy] = hm.get(candy, 0)+1
        return min(len(hm), n//2)
        # ======= Another Way ===============#
        return min(len(set(candyType)), len(candyType)//2)