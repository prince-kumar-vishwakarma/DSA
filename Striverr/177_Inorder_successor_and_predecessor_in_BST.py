# 177. Inorder successor and predecessor in BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def succPredBST(self, root, key):
        #your code goes here
        successor = None
        while root:
            if root.val <= key:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor