class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqNums = {}

        for i in range(len(nums)):
            freqNums[nums[i]] = 1 + freqNums.get(nums[i],0)

        new_dict = list(dict(sorted(freqNums.items(), key=lambda item:item[1])).keys())[::-1]

        return new_dict[:k]