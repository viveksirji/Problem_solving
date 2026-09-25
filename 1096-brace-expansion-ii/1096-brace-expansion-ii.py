class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def expand(s):
            if "{" not in s:
                return [s]

            start = -1
            count = 0

            for i in range(len(s)):
                if s[i] == "{":
                    if count == 0:
                        start = i
                    count += 1
                elif s[i] == "}":
                    count -= 1
                    if count == 0:
                        end = i
                        break

            inside = s[start + 1:end]
            parts = []
            temp = ""
            level = 0

            for ch in inside:
                if ch == "{":
                    level += 1
                elif ch == "}":
                    level -= 1

                if ch == "," and level == 0:
                    parts.append(temp)
                    temp = ""
                else:
                    temp += ch

            parts.append(temp)

            answers = []

            for part in parts:
                for value in expand(part):
                    left = s[:start]
                    right = s[end + 1:]

                    for x in expand(left + value + right):
                        answers.append(x)

            return answers

        return sorted(set(expand(expression)))