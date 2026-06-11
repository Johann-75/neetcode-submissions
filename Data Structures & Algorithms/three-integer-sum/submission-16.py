class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        a = 0
        
        while a < len(nums):
            b = a + 1
            c = len(nums)-1
            while a<b<c:
                if nums[b] + nums[c] + nums[a] > 0:
                    c = c - 1
                    continue
                elif nums[b] + nums[c] + nums[a] < 0:
                    b = b + 1
                    continue
                combo = [nums[a],nums[b],nums[c]]
                if combo not in result:
                    result.append(combo)
                b = b + 1
                    # c = c - 1
                # else:
                #     break
            a+=1



        return result

        