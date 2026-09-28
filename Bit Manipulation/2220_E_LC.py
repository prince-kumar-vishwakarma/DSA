# 2220. Minimum Bit Flips to Convert Number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flip = 0
        while start!=0 or goal!=0:
            if start&1 != goal&1:
                flip += 1
            start >>= 1
            goal >>= 1
        return flip


        