class Solution:
    def isValid(self, s: str) -> bool:
        PARENTHESES = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        
        stack = []

        for character in s:
            if character in PARENTHESES.keys():
                stack.append(character)
            elif character in PARENTHESES.values():
                try:
                    last_character = stack.pop()
                except IndexError:
                    return False
                
                if PARENTHESES[last_character] != character:
                    return False

        return len(stack) == 0
