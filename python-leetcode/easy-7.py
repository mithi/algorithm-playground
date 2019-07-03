"""
Given an integer array nums, find the contiguous subarray 
(containing at least one number) 
which has the largest sum and return its sum.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        
        running = nums[0]
        maxsum = nums[0]
        
        for i in nums[1:]:
            running = max(i, running + i)
            maxsum = max(maxsum, running)
        
        return maxsum
        
