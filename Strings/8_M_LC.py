# 8. String to Integer (atoi)

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        digit = 0
        gotDigit = False
        for c in s:
            if c == " " and not gotDigit: continue
            if c == "-" or c == "+": 
                if gotDigit: break
                gotDigit = True
                sign = -1 if c=="-" else 1
            elif "0" <= c <= "9":
                gotDigit = True
                digit = digit*10 + int(c)
            else:
                break
        ans = digit*sign
        if ans>(2**31 - 1):
            ans = (2**31 - 1)
        if ans < (-2**31):
            ans = (-2**31)
        return ans


        