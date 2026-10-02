class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result = []

        def generate(open, close, current):

            # Base condition
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add opening bracket
            if open < n:
                generate(open + 1, close, current + "(")

            # Add closing bracket
            if close < open:
                generate(open, close + 1, current + ")")

        generate(0, 0, "")

        return result