# 230. Kth Smallest Element in a BST


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # def dfs(root):
        #     if not root:
        #         return []
        #     return dfs(root.left) + [root.val] + dfs(root.right)
        # arr = dfs(root)
        # return arr[k-1]
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0: return root.val
            root = root.right
        return -1


        