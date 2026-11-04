# 94. Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        # return (
        #     self.inorderTraversal(root.left)+
        #     [root.val]+
        #     self.inorderTraversal(root.right)
        # ) 

        inorder = []

        cur = root
        while cur:
            if cur.left is None:
                inorder.append(cur.val)
                cur = cur.right
            else:
                temp = cur.left
                while temp.right and temp.right != cur:
                    temp = temp.right
                if temp.right is None:
                    temp.right = cur
                    cur = cur.left
                else:
                    temp.right = None
                    inorder.append(cur.val)
                    cur = cur.right
        return inorder
            
        




        