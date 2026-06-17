class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()


        j = 1
        k = 1
        print(nums)
        for i in range(0,len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                j += 1
            
            elif nums[i] == nums[i+1]:
                continue
            
            else:
                k = max(j,k)
                j = 1
        
        return max(j,k)