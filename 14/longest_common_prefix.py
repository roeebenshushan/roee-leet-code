class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ""

        for index in range(len(strs[0])):
            prefixes = [
                string[:index + 1] 
                for string in strs
            ]

            if len(set(prefixes)) == 1:
                common_prefix = prefixes[0]
            else:
                break

        return common_prefix
