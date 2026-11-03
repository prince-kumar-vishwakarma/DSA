# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # def f(node):
        #     if not node: return []
        #     return f(node.left) + [node.val] + f(node.right)
        # arr = f(root)
        # l, h = 0, len(arr)-1
        # while l<h:
        #     v = arr[l] + arr[h]
        #     if v == k:
        #         return True
        #     elif v<k:
        #         l += 1
        #     else:
        #         h -= 1
        # return False
        seen = set()
        def dfs(node):
            if not node: return False
            if k-node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
        