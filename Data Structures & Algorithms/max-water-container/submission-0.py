class Solution:
    def maxArea(self, heights: List[int]) -> int:
        volume = 0
        volumes = []
        start,end = 0,len(heights)

        while start < end:
            for i in range(start+1,end):
                a,b = heights[start],heights[i]
                volume = min(a,b) * (i-start)
                # print(a,b,"->",volume)
                volumes.append(volume)
            start+=1
            
        return max(volumes)