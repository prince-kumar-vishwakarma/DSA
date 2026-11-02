# 235. Lowest Common Ancestor of a Binary Search Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = root
        
        while ans:
            if ans.val>p.val and ans.val>q.val:
                ans = ans.left
            elif ans.val<p.val and ans.val<q.val:
                ans = ans.right
            else:
                return ans
        return ans


        