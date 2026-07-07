# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = []
        curr = root
        queue = deque([root])

        while queue:
            node = queue.popleft()
            nodes.append(node.val if node else "N")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(map(str,nodes))

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        sep_nodes = data.split(",")
        sep_nodes = [int(n) if n!="N" else None for n in sep_nodes]

        if sep_nodes[0] is None:
            return None
        root = TreeNode(sep_nodes[0])
        queue = deque([root])
        i = 1

        while queue and i<len(sep_nodes):
            node = queue.popleft()
            if sep_nodes[i] is not None:
                node.left = TreeNode(sep_nodes[i])
                queue.append(node.left)
            i = i + 1
            if sep_nodes[i] is not None:
                node.right = TreeNode(sep_nodes[i])
                queue.append(node.right)
            i = i + 1
        return root
            







