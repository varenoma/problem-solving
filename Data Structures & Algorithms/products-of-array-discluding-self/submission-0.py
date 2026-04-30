class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        x = 1
        for i in range(len(nums)):
            prefix[i] = x
            x *= nums[i]
        print(prefix)

        x = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = x
            x *= nums[i]
        print(suffix)

        result = []

        for i in range(len(nums)):
            x = prefix[i]
            y = suffix[i]
            result.append(y*x)

        return result








