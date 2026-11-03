# 105. Construct Binary Tree from Preorder and Inorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        i = 0
        def tree(low, high):
            nonlocal i
            if low==high: return None
            val = preorder[i]
            i+= 1
            mid = pos[val]
            root = TreeNode(val, tree(low,mid), tree(mid+1,high))
            return root
        return tree(0, len(preorder))




        

        