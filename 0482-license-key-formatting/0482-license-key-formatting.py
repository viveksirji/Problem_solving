class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        s = s.replace("-", "").upper()

        first = len(s) % k

        result = ""

        if first != 0:
            result = s[:first]
            s = s[first:]

        for i in range(0, len(s), k):
            if result != "":
                result += "-"
            result += s[i:i+k]

        return result