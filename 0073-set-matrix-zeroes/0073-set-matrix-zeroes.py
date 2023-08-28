class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zrows = set()
        zcols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zrows.add(i)
                    zcols.add(j)
        for i in zrows:
            matrix[i] = [0] * len(matrix[0])
        for j in zcols:
            for i in range(len(matrix)):
                matrix[i][j] = 0 



                    
                    