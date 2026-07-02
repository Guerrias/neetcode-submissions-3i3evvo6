class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:

        if self.min_heap and self.min_heap[0] > num:
            heapq.heappush(self.max_heap, -num)
        else : 
            heapq.heappush(self.min_heap, num)
        
        """ balance """
        if len(self.max_heap) > len(self.min_heap) + 1 :
            heapq.heappush(self.min_heap, -self.max_heap[0])
            heapq.heappop(self.max_heap)
        elif len(self.min_heap) > len(self.max_heap) + 1 :
            heapq.heappush(self.max_heap, -self.min_heap[0])
            heapq.heappop(self.min_heap)


    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return - self.max_heap[0]
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0]
        else :
            return (- self.max_heap[0] + self.min_heap[0]) / 2