class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        nums.sort()

        def bt(i: int):
            res.append(curr[:])
            if i == len(nums):
                return
            for idx in range(i, len(nums)):
                if idx == i or nums[idx] != nums[idx - 1]:
                    curr.append(nums[idx])
                    bt(idx + 1)
                    curr.pop()

        bt(0)
        return res    