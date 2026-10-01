# 222. Count Complete Tree Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if not root: return 0
        elif not root.left: return 1
        def leftH(root):
            h = 0
            while root:
                h+=1
                root = root.left
            return h
        def rightH(root):
            h = 0
            while root:
                h+=1
                root = root.right
            return h
        def height(root):
            lh = leftH(root)
            if lh == rightH(root):
                return (2**lh)-1
            return 1 + height(root.left) + height(root.right)
        return height(root)

        