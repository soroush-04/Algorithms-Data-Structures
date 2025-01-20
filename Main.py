"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums2 = set(nums)

        if len(nums) == len(nums2):
            return False
        else:
            return True
        