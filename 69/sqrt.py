class Solution:
    def mySqrt(self, x: int) -> int:
        top = x
        bottom = 0

        while bottom <= top:
            candidate = (bottom + top) // 2
            pow = candidate * candidate
            
            if pow == x:
                return candidate
            elif pow < x:
                bottom = candidate + 1
            else:
                top = candidate - 1

        return top
