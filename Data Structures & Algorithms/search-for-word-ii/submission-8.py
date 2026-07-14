class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEndOfWord = False

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.isEndOfWord = True  

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        result, visited = set(), set()

        def dfs(r,c,node, word_so_far):
            if (r < 0 or c < 0 or r == rows or c == cols or 
                (r,c) in visited or
                board[r][c] not in node.children):
                return
            visited.add((r,c))

            node = node.children[board[r][c]]
            word_so_far += board[r][c]

            if node.isEndOfWord:
                result.add(word_so_far)

            dfs(r+1,c,node,word_so_far)
            dfs(r-1,c,node,word_so_far)
            dfs(r,c+1,node,word_so_far)
            dfs(r,c-1,node,word_so_far)
            
            visited.remove((r,c))
                        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(result)            