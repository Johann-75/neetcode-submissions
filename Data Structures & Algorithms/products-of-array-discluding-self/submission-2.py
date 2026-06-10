class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1]*len(nums), [1]*len(nums)

        cumulative_prefix_prod = 1
        for i in range(len(nums)):
            cumulative_prefix_prod = cumulative_prefix_prod * nums[i]
            prefix[i] = cumulative_prefix_prod

        cumulative_postfix_prod = 1
        for j in range(len(nums)-1,-1,-1):
            cumulative_postfix_prod = cumulative_postfix_prod * nums[j]
            postfix[j] = cumulative_postfix_prod

        result = [1]*len(nums)
        for k in range(len(nums)):
            if k-1 < 0:
                before = 1
            else:
                before = prefix[k-1]
            if k+1 > len(nums)-1:
                after = 1
            else:
                after = postfix[k+1]
            result[k] = before * after


        return result
