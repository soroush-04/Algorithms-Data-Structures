"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""

from __future__ import annotations
from typing import List, Optional


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path):
            print("CALL:", path)

            if len(path) == len(nums):
                print("ADD:", path)
                res.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
                print("BACKTRACK:", path)

        backtrack([])

        return res


test = Solution()
test.permute([1, 2, 3])
