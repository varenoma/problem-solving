"""
Space: O(n)
Time: O(2n) => O(n)

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) # Space: O(n)

        x = 1
        for i in range(len(nums)): # Time O(n)
            result[i] = x
            x *= nums[i]

        x = 1
        for i in range(len(nums)-1, -1, -1): # Time O(n)
            result[i] *= x
            x *= nums[i]

        return result








