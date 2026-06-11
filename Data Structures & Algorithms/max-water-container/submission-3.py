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
            if max(volume,maxVolume) == volume:
                maxVolume = volume
            right = right - 1
            if right == left:
                left = left + 1
                right = len(heights) - 1

        return maxVolume