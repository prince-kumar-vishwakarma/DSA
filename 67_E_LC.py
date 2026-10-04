# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ""
        i,j = len(a)-1, len(b)-1
        while i>=0 or j>=0:
            x = int(a[i]) if i>=0 else 0
            y = int(b[j]) if j>=0 else 0
            total = x+y+carry
            ans += str(total%2)
            carry = total//2
            i-=1
            j-=1
        if carry:
            ans += "1"
        return ans[::-1]

        