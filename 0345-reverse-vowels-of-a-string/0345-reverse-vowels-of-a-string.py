class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = "aeiouAEIOU"

        s = list(s)

        i = 0
        j = len(s) - 1

        while i < j:

            # Move i until we find a vowel
            if s[i] not in vowels:
                i += 1
                continue

            # Move j until we find a vowel
            if s[j] not in vowels:
                j -= 1
                continue

            # Both are vowels → swap
            s[i], s[j] = s[j], s[i]

            i += 1
            j -= 1

        return "".join(s)