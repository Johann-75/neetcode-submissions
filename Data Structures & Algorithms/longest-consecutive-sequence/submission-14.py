class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        freqCounter = {}
        for k in range(len(nums)):
            freqCounter[nums[k]] = 1 + freqCounter.get(nums[k],0)

        nums = sorted(list(freqCounter.keys()))

        print(nums)
        # currentStreak = 1
        # streak = []

        # for i in range(1,len(nums)):
        #     if nums[i] - nums[i-1] == 1:
        #         currentStreak = currentStreak + 1
        #         if i == len(nums) - 1:
        #             streak.append(currentStreak)
        #     else:
        #         streak.append(currentStreak)
        #         currentStreak = 1
        # if len(streak)==0:
        #     return currentStreak
        # else:
        #     return max(streak)

        bestStreak = 1
        currentStreak = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                currentStreak += 1
            else:
                bestStreak = max(bestStreak, currentStreak)
                currentStreak = 1

        bestStreak = max(bestStreak, currentStreak)
        return bestStreak