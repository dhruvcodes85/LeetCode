class Solution:
    def secondHighest(self, s: str) -> int:
        slargest = -1
        largest = -1
        for num in s:
            if num.isdigit():
                val = int(num)
                if val > largest:
                    slargest = largest
                    largest = val
                elif val < largest and val > slargest:
                    slargest = val
        return slargest