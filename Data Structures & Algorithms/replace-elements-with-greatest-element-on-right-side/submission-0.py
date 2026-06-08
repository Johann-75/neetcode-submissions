class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = []
        for i in range(1,len(arr)):
            new_arr.append(max(arr[i:]))

        new_arr.append(-1)

        return new_arr
