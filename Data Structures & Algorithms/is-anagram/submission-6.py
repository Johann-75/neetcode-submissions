class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_chars = []
        # t_chars = []
        if len(s)!=len(t):
            return False

        # for i in s:
        #     if i not in s_chars:
        #         s_chars.append(i)
        #     else:
        #         continue
        # for j in t:
        #     if j not in t_chars:
        #         t_chars.append(j)
        #     else:
        #         continue
        # s_chars.sort()
        # t_chars.sort()
        s=sorted(s)
        t=sorted(t)
        # for k in range(len(s_chars)):
        #     if s_chars[k] == t_chars[k]:
        #         continue
        #     else:
        #         return False
        for k in range(len(s)):
            if s[k] == t[k]:
                continue
            else:
                return False
        return True
        