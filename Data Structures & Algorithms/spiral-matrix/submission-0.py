class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, m = 0, len(matrix) - 1
        j, n = 0, len(matrix[0]) - 1
        
        res = []
        while i <= m and j <= n:
            self.print_row(j, n, 1, i, res, matrix)
            self.print_col(i + 1, m, 1, n, res, matrix)
            if i != m:
                self.print_row(n - 1, j, -1, m, res, matrix)
            if j != n:
                self.print_col(m - 1, i + 1, -1, j, res, matrix)

            i += 1
            j += 1
            m -= 1
            n -= 1
        return res

    def print_row(self, l, r, step, row, res, matrix):
        for i in range(l, r + step, step):
            res.append(matrix[row][i])
        
    def print_col(self, t, d, step, c, res, matrix):
        for i in range(t, d + step, step):
            res.append(matrix[i][c])
    


            