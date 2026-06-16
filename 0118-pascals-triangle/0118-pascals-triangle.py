class Solution:
    def generateRow(self, row: int) -> List[int]:
        ansRow = []
        ans = 1
        ansRow.append(1)
        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col
            ansRow.append(ans)
        return ansRow

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows + 1):
            ans.append(self.generateRow(i))
        
        return ans