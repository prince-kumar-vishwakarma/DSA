# 987. Vertical Order Traversal of a Binary Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        queue = deque()
        queue.append((root, 0, 0))
        hm = {}
        while queue:
            node, x, y = queue.popleft()
            if x not in hm:
                hm[x] = []
            hm[x].append((y, node.val))
            
            if node.left:
                queue.append((node.left, x-1, y+1))
            if node.right:
                queue.append((node.right, x+1, y+1))
        
        ans = []
        for x in sorted(hm):
            hm[x].sort()
            ans.append([val for y, val in hm[x]])
        return ans
        
        
        
            
            

        