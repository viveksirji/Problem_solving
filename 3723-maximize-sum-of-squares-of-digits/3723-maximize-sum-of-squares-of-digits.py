
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > num * 9:
            return ""

        nines = sum // 9
        remainder = sum % 9

        result = "9" * nines

        if remainder > 0:
            result += str(remainder)

        result += "0" * (num - len(result))

        return result
