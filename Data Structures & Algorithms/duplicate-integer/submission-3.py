class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for item in nums:
            if item not in hash_map:
                hash_map[item] = 1
            else:
                return True
        return False