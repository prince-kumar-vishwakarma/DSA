# 29. Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = True
        if dividend<0: pos = not pos
        if divisor<0: pos = not pos
        n, d = abs(dividend), abs(divisor)
        ans = 0
        while n>=d:
            cnt = 0
            while n >= (d<<(cnt+1)):
                cnt += 1
            ans += (1<<cnt)
            n -= (d<<cnt)
        if ans>=2**31:
            return  2**31 - 1 if pos else -2**31
        return ans if pos else -ans


