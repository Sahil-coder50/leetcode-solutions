class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l = len(matrix)

        for row in range(l-1):
            for col in range(row+1, l):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for i in range(l):
            matrix[i].reverse()

        



        