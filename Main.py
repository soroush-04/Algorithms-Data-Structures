"""
climbing stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
how many distinct ways can you climb to the top?
"""


class Solution:
    def climb_stairs(self, n: int) -> int:
        a, b = 1, 2

        if n == 1:
            return 1

        for _ in range(2, n):
            a, b = b, a + b

        return b


test = Solution()
print(test.climb_stairs(5))
