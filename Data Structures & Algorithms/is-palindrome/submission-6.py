class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        # print(s)
        left, right = 0, len(s)-1
        while left<right:
            if s[left] != s[right]:
                return False
            left = left+1
            right = right-1
        return True