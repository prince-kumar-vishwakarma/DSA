# 435. Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        have = 1
        last = intervals[0][1]
        i = 1
        n = len(intervals)
        while i<n:
            if last<=intervals[i][0]:
                have += 1
                last = intervals[i][1]
            i += 1
        return n-have