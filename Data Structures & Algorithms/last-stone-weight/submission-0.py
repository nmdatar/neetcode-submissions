class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = - heapq.heappop(stones), - heapq.heappop(stones)
            print(x, y)
            if y < x:
                heapq.heappush(stones, y - x)
        
        return -heapq.heappop(stones) if len(stones) == 1 else 0
        