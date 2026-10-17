class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, curr = [], []
        self.bt(0, nums, res, curr, target)
        return res
    def bt(self, i: int, nums: List[int], res: List[List[int]], curr: List[int], s: int):
        if s == 0:
            res.append(curr[:])
        
        if i == len(nums) or s < 0:
            return
        
        for idx in range(i, len(nums)):
            if idx == 0 or nums[idx] != nums[idx-1]:
                curr.append(nums[idx])
                self.bt(idx, nums, res, curr, s - nums[idx])
                curr.pop()
        