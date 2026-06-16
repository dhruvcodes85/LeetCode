class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ansRow = []
        ans = 1
        ansRow.append(ans)
        rowIndex += 1
        for col in range(1, rowIndex):
            ans = ans * (rowIndex - col)
            ans  = ans // col 
            ansRow.append(ans)
        
        return ansRow