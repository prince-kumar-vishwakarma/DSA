# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def allRootToLeaf(self, root):
        #your code goes here
        ans = []
        def f(root, arr, ans):
            if not root: return
            if not root.left and not root.right: 
                arr.append(root.data)
                ans.append(arr[:])
                arr.pop()
                return 
            arr.append(root.data)
            f(root.left, arr, ans)
            f(root.right, arr, ans)
            arr.pop()
        f(root, [], ans)
        return ans
