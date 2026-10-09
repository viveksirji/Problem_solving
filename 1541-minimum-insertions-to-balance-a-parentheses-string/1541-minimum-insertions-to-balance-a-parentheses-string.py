
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        need = 0

        for ch in s:

            # Every opening parenthesis needs two closing parentheses
            if ch == '(':
                need += 2

                # If need is odd, a previous closing parenthesis
                # has matched only one of the required two
                if need % 2 == 1:
                    insertions += 1
                    need -= 1

            else:
                need -= 1

                # Extra closing parenthesis: insert an opening one
                if need == -1:
                    insertions += 1
                    need = 1

        # Insert any closing parentheses still required
        return insertions + need