"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        intervals.sort(key=lambda x:x.start)
        nextStart = math.inf
        count = 0

        for i, interval in enumerate(intervals):
            heapq.heappush(heap, interval.end)
            if i == len(intervals) -1:
                nextStart = math.inf
            else:
                nextStart = intervals[i+1].start
            
            #print(heap, nextStart)
            count = max(count, len(heap))

            while heap and heap[0] <= nextStart:
                heapq.heappop(heap)
    
            #print(heap, len(heap))
            
        return count
            