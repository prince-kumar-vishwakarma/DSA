# 3498. Reverse Degree of a String
# https://leetcode.com/problems/reverse-degree-of-a-string/description/

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, n in enumerate(s, 1):
            ans += (ord("z")-ord(n)+1) * i
        return ans