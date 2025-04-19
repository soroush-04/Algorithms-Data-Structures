# n-queen problem
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

"""


class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]

        if n == 0:
            return 0
        if n == 1:
            return 1

        for _ in range(2, n + 1):
            temp = dp[0]
            dp[0] = dp[1]
            dp[1] = temp + dp[0]

        return dp[1]


test = Solution()
print(test.fib(8))

"""
n = 3
0   1
temp 0
1

"""
