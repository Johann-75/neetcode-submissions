class Solution:
    def merge_sort(self,arr: List[int]) -> List[int]:
        if len(arr)<=1:
            return arr
        
        mid = len(arr)//2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left,right)

    def merge(self, left: List[int],right: List[int]) -> List[int]:
        merged = []
        i = 0
        j = 0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged
        

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

        