"""
Space: O(3n) => O(n)
Time: O(3n) => O(n)

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums) # Space: O(n)
        suffix = [1] * len(nums) # Space: O(n)

        x = 1
        for i in range(len(nums)): # Time O(n)
            prefix[i] = x
            x *= nums[i]

        x = 1
        for i in range(len(nums)-1, -1, -1): # Time O(n)
            suffix[i] = x
            x *= nums[i]

        result = [] # Space: O(n)

        for i in range(len(nums)): # Time O(n)
            x = prefix[i]
            y = suffix[i]
            result.append(y*x)

        return result








