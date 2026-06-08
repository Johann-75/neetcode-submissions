class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        max_val = 0
        max_key = 0

        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        # print(frequency)
        for key,value in frequency.items():
            if value>=max_val:
                max_val = value
                max_key = key

        return max_key