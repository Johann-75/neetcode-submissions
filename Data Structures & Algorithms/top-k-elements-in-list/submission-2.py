class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqNums = {}

        for i in range(len(nums)):
            freqNums[nums[i]] = 1 + freqNums.get(nums[i],0)

        new_dict = [x[0] for x in sorted(freqNums.items(), key=lambda item: item[1],reverse=True)]

        return new_dict[:k]