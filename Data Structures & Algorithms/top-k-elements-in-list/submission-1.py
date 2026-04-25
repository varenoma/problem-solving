class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for x in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for num, i in count.items():
            freq[i].append(num)

        result = []
        for freq_i in range(len(freq)-1, 0, -1):
            for n in freq[freq_i]:
                result.append(n)

                if len(result) == k:
                    return result
        
        return []


        print(count)
        print(freq)

        return []