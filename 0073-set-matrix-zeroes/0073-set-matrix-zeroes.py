class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        index = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    index.append((i, j))
        print(index)
        for i in range(len(index)):
            idx = index[i][0]
            for j in range(len(matrix[0])):
                matrix[idx][j] = 0

        for i in range(len(index)):
            idx = index[i][1]
            for j in range(len(matrix)):
                matrix[j][idx] = 0

        print(matrix)


        