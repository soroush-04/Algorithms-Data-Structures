"""
Number of 1 Bits
"""

from typing import List


# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         bin_n = bin(n)[2:]
#         hamming_weight = 0

#         for i in bin_n:
#             if i == '1':
#                 hamming_weight += 1

#         return hamming_weight


class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0

        while n:
            if n & 1:
                sum += 1
            n >>= 1

        return sum


test = Solution()
print(test.hammingWeight(5))
