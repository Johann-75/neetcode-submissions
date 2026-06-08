class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b=[]
        for i in nums:
            if i in b:
                return True
            else:
                b.append(i)
        return False