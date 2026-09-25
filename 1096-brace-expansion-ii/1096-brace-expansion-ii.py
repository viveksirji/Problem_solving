class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def expand(s):
            if "{" not in s:
                return [s]

            start = s.rfind("{")
            end = s.find("}", start)

            inside = s[start + 1:end]
            parts = inside.split(",")

            result = []

            for part in parts:
                new_s = s[:start] + part + s[end + 1:]
                result += expand(new_s)

            return result

        return sorted(set(expand(expression)))