class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = sorted(list(set(nums)))
        print(arr)
        n=1
        seq = []
        
        if len(arr)>1:
            for i in range(len(arr)-1):
                if arr[i+1] == arr[i] + 1:
                    n+=1
                else:
                    # seq.append(n)
                    n=1
                seq.append(n)
            return max(seq)
        else:
            return len(arr)