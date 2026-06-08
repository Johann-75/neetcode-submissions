class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for a in s:
            if a not in hash_s:
                hash_s[a] = 1
            else:
                hash_s[a] += 1

        for b in t:
            if b not in hash_t:
                hash_t[b] = 1
            else:
                hash_t[b] += 1

        return hash_s == hash_t
        