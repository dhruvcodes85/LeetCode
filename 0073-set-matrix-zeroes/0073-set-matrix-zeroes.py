class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ## from better solution
        # row = [0] * len(matrix) --> row[..][0]
        # col = [0] * len(matrix[0]) --> col[0][..]  
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1 ## Extra space for marking column as zero
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # Mark the ith row (Check the better solution)
                    matrix[i][0] = 0

                    # Mark the jth col expect [0][0] 
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        print(matrix)
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix [i][j] = 0

        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
