class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for px, py in points:
            heapq.heappush(h, [-(px ** 2 + py ** 2), [px, py]])
            if len(h) > k:
                heapq.heappop(h)
        
        return [p[1] for p in h]
        
        
