class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        m, n = len(board), len(board[0])

        def is_valid(r:int, c:int):
            return 0 <= r < m and 0 <= c < n

        def bt(i: int, r:int, c:int):
            if i == len(word):
                return True
            
            if not is_valid(r, c) or (r, c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r, c))
            for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                if bt(i + 1, r + dx, c + dy): return True

            visited.remove((r, c))
            return False
        
        for i in range(m):
            for j in range(n):
                if bt(0, i, j):
                    return True
        
        return False
            
            
        
