class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashMap = {}

        # for i in range(len(nums)):
        #     hashMap[nums[i]] = 1 + hashMap.get(nums[i],0)
        
        # for j in hashMap.values():
        #     if j>1:
        #         return True
        # return False

        return len(nums) != len(set(nums))
