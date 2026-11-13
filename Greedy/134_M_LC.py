# 134. Gas Station

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(cost) > sum(gas): return -1
        n = len(gas)
        i = 0
        while i < n:
            tank = gas[i] - cost[i]
            j = i + 1

            while j < n:
                if tank < 0:
                    break
                tank += gas[j] - cost[j]
                j += 1

            if tank >= 0:
                return i
            i = j

        return -1

        