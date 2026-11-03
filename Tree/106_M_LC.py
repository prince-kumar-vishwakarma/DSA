# 106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {v:i for i,v in enumerate(inorder)}
        i = len(postorder) -1
        def build(low, high):
            nonlocal i
            if low == high: return None
            root_val = postorder[i]
            i -= 1
            mid = pos[root_val]
            root = TreeNode(root_val)
            root.right = build(mid + 1, high)
            root.left = build(low, mid)
            return root

        return build(0, len(inorder))
        