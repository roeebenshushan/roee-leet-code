class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for letter in reversed(s):
            if letter != " ":
                length += 1
            elif length:
                break

        return length
