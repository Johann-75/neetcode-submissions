class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxVolume = 0

        while left < right:
            width = right-left
            height = min(heights[left],heights[right])
            volume = height*width
            # print(left,right,heights[left],heights[right],volume, maxVolume)
            maxVolume = max(maxVolume,volume)
            if height == heights[left]:
                left = left + 1
            elif height == heights[right]:
                right = right - 1
            # right = right - 1
            # if right == left:
            #     left = left + 1
            #     right = len(heights) - 1

        return maxVolume