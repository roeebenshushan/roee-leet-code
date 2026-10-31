class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        digits = []
        index_a = len(a) - 1
        index_b = len(b) - 1

        while index_a >= 0 or index_b >= 0 or carry:
            curr_a = int(a[index_a]) if index_a >= 0 else 0
            curr_b = int(b[index_b]) if index_b >= 0 else 0

            digit = curr_a + curr_b + carry
            carry = digit // 2
            digits.append(str(digit % 2))

            index_a -= 1
            index_b -= 1

        return "".join(reversed(digits))
