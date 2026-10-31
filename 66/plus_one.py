class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        reminder = 1

        for index in reversed(range(len(digits))):
            addition = digits[index] + reminder
            reminder = addition // 10

            digits[index] = addition % 10

        return [1] + digits if reminder else digits 
