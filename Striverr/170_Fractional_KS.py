# 174. Fractional Knapsack

class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        vbw = []
        for i,(v,w) in enumerate(zip(val, wt)):
            vbw.append((v/w, i))
        vbw.sort(reverse=True)
        ans = 0
        for (v,i) in vbw:
            if cap>=wt[i]:
                cap -= wt[i]
                ans += val[i]
            else:
                ans += v*cap
                break
        return ans
            


