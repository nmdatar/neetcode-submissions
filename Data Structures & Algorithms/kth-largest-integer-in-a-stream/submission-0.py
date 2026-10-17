from heapq import heapify, heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.h = []
        for n in nums:
            heappush(self.h, n)

        while len(self.h) > k:
            heappop(self.h)

    def add(self, val: int) -> int:
        heappush(self.h, val)

        while len(self.h) > self.k:
            heappop(self.h)
        
        return self.h[0]
        
