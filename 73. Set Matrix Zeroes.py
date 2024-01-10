class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows_to_zero = set()
        cols_to_zero = set()

        ROWS, COLS = len(matrix), len(matrix[0])

        # Identify positions of zero elements
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows_to_zero.add(i)
                    cols_to_zero.add(j)

        # Update rows to zero
        for row in rows_to_zero:
            for col in range(COLS):
                matrix[row][col] = 0
            
        # Update columns to zero
        for col in cols_to_zero:
            for row in range(ROWS):
                matrix[row][col] = 0
            
        