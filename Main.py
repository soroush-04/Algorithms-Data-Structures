"""
1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

from __future__ import annotations
from typing import List, Optional


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxi = 0
        zero_counter = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_counter += 1

            while zero_counter > k:
                if nums[right] == 0:
                    zero_counter -= 1
                left += 1

            maxi = max(maxi, right - left + 1)
