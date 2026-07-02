# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        levelNodes = [[root.val]]
        while queue:
            currentLevel = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    currentLevel.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    currentLevel.append(node.right.val)
            if currentLevel:
                levelNodes.append(currentLevel)
        return levelNodes