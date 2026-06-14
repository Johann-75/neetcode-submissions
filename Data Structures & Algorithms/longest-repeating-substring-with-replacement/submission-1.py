class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = left
        result = 0


        while left<=right<len(s):
            substring = s[left:right+1]
            windowSize = len(substring)
            hashMap = {}
            for i in range(len(substring)):
                hashMap[substring[i]] = 1 + hashMap.get(substring[i],0)
            maxCharCount = max(hashMap.values())
            
            if windowSize - maxCharCount <= k:
                result = max(result,windowSize)
                right = right + 1
            else:
                left = left+1

        return result

            

