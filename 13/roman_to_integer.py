class Solution:
    SUBSTRACTABLE_DIGITS = {
        "I": ["V", "X"],
        "X": ["L", "C"],
        "C": ["D", "M"]
    }
    
    ROMAN_DIGITS = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    def romanToInt(self, s: str) -> int:
        num = 0

        for index in range(len(s)):
            try:
                roman_digit = s[index]
                next_roman_digit = s[index + 1]
                
                if next_roman_digit in self.SUBSTRACTABLE_DIGITS[roman_digit]:
                    num -= self.ROMAN_DIGITS[roman_digit]
                else:
                    raise IndexError()
            except (IndexError, KeyError):
                num += self.ROMAN_DIGITS[roman_digit]

        return num

print(Solution().romanToInt("MCMXCIV")) # 1994