# 662. Maximum Width of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        queue = deque([(root, 0)])
        width = 1
        while queue:
            n = len(queue)
            first,second = 0, 0
            for i in range(n):
                node, x = queue.popleft()
                if i == 0:
                    first = abs(x)
                if i == n-1:
                    second = abs(x)
                if node.left:
                    queue.append((node.left, 2*x + 1))
                if node.right:
                    queue.append((node.right, 2*x + 2))
            if n > 1:
                width = max(width, second-first+1)
        return width
                

                


        