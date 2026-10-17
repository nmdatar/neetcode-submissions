class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        self.bt(0, nums, res, curr)
        return res
    def bt(self, idx: int, nums: List[int], res: List[List[int]], curr: List[int]):
        res.append(curr[:])
        if idx == len(nums):
            return 
        
        for i in range(idx, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            curr.append(nums[i])
            self.bt(i+1, nums, res, curr)
            curr.pop()

