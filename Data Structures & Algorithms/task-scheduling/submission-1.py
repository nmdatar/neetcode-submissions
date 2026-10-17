class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for t in tasks:
            idx = ord(t) - ord('A')
            count[idx] += 1

        count.sort()
        maxf = count[-1]
        idle = (maxf - 1) * n

        for i in range(24, -1, -1):
            idle -= min(count[i], maxf - 1)
        
        return max(0, idle) + len(tasks)