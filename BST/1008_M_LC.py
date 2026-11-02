# 1008. Construct Binary Search Tree from Preorder Traversal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        i = 0
        n = len(preorder)
        def f(ub):
            nonlocal i
            if i == n or preorder[i] > ub:
                return None
            newNode = TreeNode(preorder[i])
            i+=1
            newNode.left = f(newNode.val)
            newNode.right = f(ub)
            return newNode
        return f(float("inf"))

        