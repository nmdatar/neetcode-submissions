class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            if self.can_finish(piles, m, h):
                r = m - 1
            else:
                l = m + 1
        return l



    def can_finish(self, piles, k, h) -> bool:
        res = 0
        for p in piles:
            res += math.ceil(p / k)
            if res > h:
                return False
        
        return True