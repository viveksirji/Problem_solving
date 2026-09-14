# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# LeetCode 374 - Guess Number Higher or Lower

class Solution:
    def guessNumber(self, n: int) -> int:

        low = 1
        high = n

        while low <= high:

            mid = (low + high) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
                # mid is too high
                high = mid - 1

            else:
                # mid is too low
                low = mid + 1
        