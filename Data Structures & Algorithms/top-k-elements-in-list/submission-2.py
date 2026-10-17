class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = defaultdict(int)
        for n in nums:
            cnts[n] += 1
        cnts = [[v, k] for k, v in cnts.items()]
        k = len(cnts) - k
        return self.quick_select(k, cnts, 0, len(cnts) - 1)

    def quick_select(self, k: int, nums: List[List[int]], l:int , r:int):
        p = l

        for i in range(l, r + 1):
            if nums[i][0] < nums[l][0]:
                p += 1
                nums[i], nums[p] = nums[p], nums[i]

        nums[l], nums[p] = nums[p], nums[l]
        
        if p == k:
            return [n[1] for n in nums[k:]]
        elif p < k:
            return self.quick_select(k, nums, p + 1, r)
        else:
            return self.quick_select(k, nums, l, p - 1)

        


"""
k = 2
[3, 6, 7, 1, 8]

p = 0, r = 3, l = 0
i = 1 

p = 0, i = 2

p = 1, i = 3

swap(p, )

"""

