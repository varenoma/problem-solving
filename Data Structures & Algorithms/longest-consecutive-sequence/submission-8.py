class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        mx = 0

        for num in nums_set:
            if not num - 1 in nums_set:
                curr = num
                j = 1
                while curr + 1 in nums_set:
                    curr += 1
                    j += 1
            
                mx=max(j,mx)
        
        return mx