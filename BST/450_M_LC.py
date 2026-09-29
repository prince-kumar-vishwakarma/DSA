# 450. Delete Node in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if not root: return root
        def helper(root):
            if not root.left: return root.right
            elif not root.right: return root.left
            temp = root.left
            while temp.right:
                temp = temp.right
            temp.right = root.right
            return root.left
        if root.val == key:
            return helper(root)
        temp = root
        while temp:
            if temp.val>key:
                if temp.left and temp.left.val == key:
                    temp.left = helper(temp.left)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right and temp.right.val == key:
                    temp.right = helper(temp.right)
                    break
                else:
                    temp = temp.right
        return root
