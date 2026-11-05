class Solution:
    def climbStairs(self, n: int) -> int:
        def calculate(n, cache):
            if n in cache:
                return cache[n]
            if n < 0:
                return 0
            if n == 0:
                return 1

            cache[n] = calculate(n - 1, cache) + calculate(n - 2, cache)
            return cache[n]

        return calculate(n, {})