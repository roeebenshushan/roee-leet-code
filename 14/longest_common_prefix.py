class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ""

        for index in range(len(strs[0])):
            prefices = [
                string[:index + 1] 
                for string in strs
            ]

            if len(set(prefices)) == 1:
                common_prefix = prefices[0]
            else:
                break

        return common_prefix
