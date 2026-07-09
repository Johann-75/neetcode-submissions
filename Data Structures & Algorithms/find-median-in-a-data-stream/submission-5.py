class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        size = len(self.arr)
        if size % 2 != 0:
            return self.arr[size//2]
        else:
            right = size//2
            left = right-1
            return (self.arr[left] + self.arr[right])/2
        