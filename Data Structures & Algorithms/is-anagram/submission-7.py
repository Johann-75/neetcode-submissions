class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s=sorted(s)
        t=sorted(t)
        for k in range(len(s)):
            if s[k] == t[k]:
                continue
            else:
                return False
        return True
        