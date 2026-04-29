class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.prefix_sum = [[0]*(col + 1) for _ in range(row + 1)]
        for r in range(row):
            
            for c in range(col):
                top = self.prefix_sum[r][c + 1]
                left = self.prefix_sum[r + 1][c]
                topleft = self.prefix_sum[r ][c]
                self.prefix_sum[r + 1][c + 1] = (
                    matrix[r][c] + top + left - topleft
                )


                
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        total = self.prefix_sum[row2][col2]
        top = self.prefix_sum[row1 - 1][col2]
        left = self.prefix_sum[row2][col1 - 1]
        topleft = self.prefix_sum[row1-1][col1 -1]
        return total - top - left + topleft
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)