# 131. Palindrome Partitioning

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        def part(s, arr):
            if not s:
                ans.append(arr[:])
                return
            for i in range(1, len(s)+1):
                s1 = s[:i]
                if s1 == s1[::-1]: 
                    arr.append(s1)
                    part(s[i:], arr)
                    arr.pop()
        part(s, [])
        return ans

        