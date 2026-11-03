# 236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # ans = None
        # def find(root, p, q):
        #     nonlocal ans
        #     if not root: return 0
        #     left = find(root.left, p, q)
        #     right = find(root.right, p, q)
        #     total = left+right
        #     if p==root or q==root:
        #         total += 1
        #     if total == 2 and ans is None:
        #         ans = root 
        #     return total
        # find(root,p,q)
        # return ans

        def find(root, p, q):
            if not root: return None
            left = find(root.left, p, q)
            right = find(root.right, p, q)
            if p==root or q==root:
                return root
            if left and right:
                return root
            if left:
                return left
            if right:
                return right
            return None
        return find(root,p,q)

        
        
