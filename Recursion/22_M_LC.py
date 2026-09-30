# 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def gen(s, op, close, ans):
            if op ==  0:
                s = s+(")"*close)
                ans.append(s)
                return
            if close == 0:
                ans.append(s)
                return
            if op == close:
                s += "("
                gen(s, op-1, close, ans)
                return
            gen(s+"(", op-1, close, ans)
            gen(s+")", op, close-1, ans)
        gen("", n, n, ans)
        return ans


        