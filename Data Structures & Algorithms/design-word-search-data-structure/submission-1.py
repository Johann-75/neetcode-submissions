class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j,len(word)):
                if word[i] == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if word[i] in curr.children:
                        curr = curr.children[word[i]]
                    else:
                        return False
            return curr.isEndOfWord

        return dfs(0,self.root)
