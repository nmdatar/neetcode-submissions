class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)

        l = 1

        for i in range(len(nums)):
            arr[i] *= l
            l *= nums[i]
        
        r = 1
        for i in range(len(nums) -1 , -1, -1):
            arr[i] *= r
            r *= nums[i]
        
        return arr
