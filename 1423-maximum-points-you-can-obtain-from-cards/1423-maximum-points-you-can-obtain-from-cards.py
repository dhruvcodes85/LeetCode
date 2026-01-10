class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum, rsum = 0, 0
        rindex = len(cardPoints) - 1

        for i in range(k):
            lsum += cardPoints[i]
        
        maxSum = lsum

        for i in reversed(range(k)):
            lsum -= cardPoints[i]
            rsum += cardPoints[rindex]
            rindex -= 1

            maxSum = max(maxSum, lsum + rsum)

        return maxSum