class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashS, hashT = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i],0)
        
        for j in range(len(t)):
            hashT[t[j]] = 1 + hashT.get(t[j],0)

        if hashS == hashT:
            return True
        return False