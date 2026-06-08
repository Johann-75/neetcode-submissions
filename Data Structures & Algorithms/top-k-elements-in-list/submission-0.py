class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        max_freq = 0
        max_val = 0
        final = []

        nums_set = set(nums)

        for i in nums_set:
            freq[i] = 0

        for i in nums:
            freq[i] +=1
            
        print(freq)
            
        while k != 0:
            max_freq = 0
            max_val = 0
            for key, value in freq.items():
                if value>max_freq:
                    max_freq = value
                    max_val = key
            final.append(max_val)
            freq.pop(max_val)
            k-=1
            
        return final
            

            