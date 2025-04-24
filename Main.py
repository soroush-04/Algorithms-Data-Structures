"""
Longest Increasing Subsequence
"""

from typing import List


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [1] * n

#         for i in range(n):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)

#         return max(dp)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []

        def binary_search_left(arr, target):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        for num in nums:
            i = binary_search_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
