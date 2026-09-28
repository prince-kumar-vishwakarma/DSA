# 38. Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for i in range(1,n):
            new = ""
            cnt = 0
            ele = ""
            for a in ans:
                if ele == "":
                    ele = a
                    cnt += 1
                elif ele == a:
                    cnt += 1
                else:
                    new += f"{cnt}{ele}"
                    cnt = 1
                    ele = a
            if cnt:
                new += f"{cnt}{ele}"
            ans = new
        return ans


        