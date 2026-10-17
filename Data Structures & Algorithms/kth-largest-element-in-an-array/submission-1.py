class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        return self.quick_select(0, len(nums) - 1, k, nums)
    def quick_select(self, l:int, r:int, k:int, nums: List[int]) -> int:
        p = l

        for i in range(l, r + 1):
            if nums[i] < nums[l]:
                p += 1
                nums[i], nums[p] = nums[p], nums[i]
        
        nums[l], nums[p] = nums[p], nums[l]

        if p == k:
            return nums[k]
        elif p < k:
            return self.quick_select(p + 1, r, k, nums)
        else:
            return self.quick_select(l, p - 1, k, nums)
        