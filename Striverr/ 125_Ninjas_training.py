# 
# 125. Ninja's training

class Solution:
    def ninjaTraining(self, matrix):
        n = len(matrix)
        dp = [[-1] * 4 for _ in range(n)]

        def f(day, last_pick):
            if day == 0:
                best = 0
                for act in range(3):
                    if act != last_pick:
                        best = max(best, matrix[day][act])
                return best

            if dp[day][last_pick] != -1: return dp[day][last_pick]
            best = 0
            for act in range(3):
                if act != last_pick:
                    points = matrix[day][act] + f(day-1, act)
                    best = max(best, points)
            dp[day][last_pick] = best
            return best



        return f(n-1, 3)

