class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for m in range(len(strs)):
            hashMap = [0] * 26
            word = strs[m]
            for i in range(len(word)):
                hashMap[ord(word[i]) - ord('a')] += 1
            key = tuple(hashMap)
            if key not in groups.keys():
                groups[key] = list()
            groups[key].append(word)

        return list(groups.values())