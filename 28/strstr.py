class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # ok ok this is not a valid solution, uses slicing...
        for index in range(len(haystack)):
            try:
                if haystack[index : index + len(needle)] == needle:
                    return index
            except IndexError:
                break

        return -1