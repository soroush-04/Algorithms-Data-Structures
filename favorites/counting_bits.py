"""
Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""

from typing import List


# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         dp = [0] * (n + 1)

#         for i in range(1, n + 1):
#             x = i
#             ans = 0
#             while x:
#                 ans += x & 1
#                 x >>= 1
#             dp[i] = ans

#         return dp


class Solution:
    def count_bits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)

        return dp


test = Solution()
print(test.count_bits(5))
