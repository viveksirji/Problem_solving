class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        result = set()

        left_remove = 0
        right_remove = 0

        # Find minimum number of '(' and ')' to remove
        for ch in s:
            if ch == "(":
                left_remove += 1

            elif ch == ")":
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        def backtrack(index, path, balance, left, right):
            # Invalid because ')' is more than '('
            if balance < 0:
                return

            # No removals left
            if left == 0 and right == 0:
                remaining = s[index:]

                # Check remaining characters
                for ch in remaining:
                    if ch == "(":
                        balance += 1
                    elif ch == ")":
                        balance -= 1

                    if balance < 0:
                        return

                if balance == 0:
                    result.add("".join(path) + remaining)

                return

            if index == len(s):
                return

            ch = s[index]

            # Remove '('
            if ch == "(" and left > 0:
                backtrack(
                    index + 1,
                    path,
                    balance,
                    left - 1,
                    right
                )

            # Remove ')'
            elif ch == ")" and right > 0:
                backtrack(
                    index + 1,
                    path,
                    balance,
                    left,
                    right - 1
                )

            # Keep current character
            path.append(ch)

            if ch == "(":
                backtrack(
                    index + 1,
                    path,
                    balance + 1,
                    left,
                    right
                )
            elif ch == ")":
                backtrack(
                    index + 1,
                    path,
                    balance - 1,
                    left,
                    right
                )
            else:
                backtrack(
                    index + 1,
                    path,
                    balance,
                    left,
                    right
                )

            path.pop()

        backtrack(0, [], 0, left_remove, right_remove)

        return list(result)