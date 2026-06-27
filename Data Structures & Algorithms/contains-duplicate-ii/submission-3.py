class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_map = {}

        for i, n in enumerate(nums):
            if n in h_map and i - h_map[n] <= k:
                return True
            
            h_map[n] = i
        
        return False