# 701. Insert into a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if not root: return TreeNode(val)
        temp = root
        while temp:
            if temp.val>val:
                if not temp.left: 
                    temp.left = TreeNode(val)
                    break
                temp = temp.left
            else:
                if not temp.right: 
                    temp.right = TreeNode(val)
                    break
                temp = temp.right
        return root