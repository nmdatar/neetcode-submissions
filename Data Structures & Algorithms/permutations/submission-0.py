class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res, curr = [], []

        self.bt(curr, res, nums, visited)
        return res

    def bt(self, curr: List[int], res: List[List[int]], nums: List[int], visited: set):
        if len(curr) == len(nums):
            res.append(curr[:])
            return 
        
        for s in range(len(nums)):
            if s not in visited:
                visited.add(s)
                curr.append(nums[s])
                self.bt(curr, res, nums, visited)
                curr.pop()
                visited.remove(s)
            
