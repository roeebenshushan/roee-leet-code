class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        for pointer1 in range(len(haystack)):
            if haystack[pointer1] == needle[0]:
                flag = True
                
                for pointer2 in range(1, len(needle)):
                    haystack_pointer = pointer1 + pointer2

                    try:
                        if haystack[haystack_pointer] != needle[pointer2]:
                            flag = False
                            break
                    except IndexError:
                        return -1
                        
                if flag:
                    return pointer1
        
        return -1


print(Solution().strStr("mississippi", "issipi"))