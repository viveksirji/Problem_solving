class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:

        total = 0

        for i in range(len(timeSeries) - 1):

            gap = timeSeries[i + 1] - timeSeries[i]

            if gap < duration:
                total += gap
            else:
                total += duration

        # Add the full duration of the last attack
        total += duration

        return total