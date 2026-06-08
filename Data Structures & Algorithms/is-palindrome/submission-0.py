import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower().strip()
        s=re.sub(r'[^A-Za-z0-9]','',s)
        
        for i in range(len(s)):
            if s[i] != s[len(s)-i-1]:
                return False
            else:
                continue
        return True
