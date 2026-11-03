# 99. Recover Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        first, mid, second = None, None, None
        last = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not last:
                last = root
            else:
                if last.val>root.val:
                    if not first:
                        first = last
                        mid = root
                    else:
                        second = root
                        break
            last = root
            root = root.right
        if second:
            first.val, second.val = second.val, first.val
        else:
            first.val, mid.val = mid.val, first.val


        