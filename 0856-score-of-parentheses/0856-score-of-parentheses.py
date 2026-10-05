class Solution:
    # def scoreOfParentheses(self, s: str) -> int:
    #     stack = [0]

    #     for i in s:
    #         if i == "(":
    #             stack.append(0)
    #         else:
    #             value = stack.pop()

    #             if value == 0:
    #                 score = 1
    #             else:
    #                 score = 2 * value

    #             stack[-1] += score

    #     return stack[0]
    def scoreOfParentheses(self, s: str) -> int:
        depth = 0
        score = 0

        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
            else:
                depth -= 1

                if s[i - 1] == "(":
                    score += 2 ** depth

        return score