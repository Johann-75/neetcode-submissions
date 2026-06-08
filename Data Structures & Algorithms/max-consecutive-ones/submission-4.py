class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=1
        max_consec = []
        if len(nums)==1 and nums[0]==1:
            return 1
        elif len(nums)==1 and nums[0]==0:
            return 0
        for i in range(len(nums)-1):
            if nums[i] == 1 and nums[i+1] == 1:
                n = n+1
            elif nums[i] != nums[i+1]:
                n=1
            elif nums[i] == 0 and nums[i] == 0:
                n=0
            max_consec.append(n)
            # n=0
        return max(max_consec)