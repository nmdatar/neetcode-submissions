class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mx = 0

        s = set(nums)

        for n in s:
            if n - 1 in s:
                continue
            c = n
            while c in s:
                c += 1
                mx = max(mx, c - n)
        return mx

