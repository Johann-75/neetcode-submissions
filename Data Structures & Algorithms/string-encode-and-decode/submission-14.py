import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for i in range(len(strs)):
            encoded.append(f"{str(len(strs[i]))}#{strs[i]}")
            
        # print(encoded)
        # print("".join(encoded))
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        result, left = [], 0

        while left < len(s):
            right = left

            while s[right] != "#":
                right+=1
            length = int(s[left:right])
            result.append(s[right+1 : right+1+length])
            left = right + 1 + length

        return result