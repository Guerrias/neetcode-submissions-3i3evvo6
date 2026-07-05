class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        count = 0
        last = None

        for interval in intervals:
            if last and interval[0] < last:
                count += 1
            else:
                last = interval[1]
        return count