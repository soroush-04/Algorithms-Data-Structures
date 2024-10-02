"""You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104"""

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0 
        left = 0
        max_sum = float('-inf')
        
        if len(nums) < k:
            return 0
        
        for right in range(len(nums)):
            sum += nums[right]
            if right - left + 1 == k:
                max_sum = max(sum, max_sum)
                sum -= nums[left]
                left += 1
        
        return max_sum / k