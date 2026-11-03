# 173. Binary Search Tree Iterator


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        # self.root = root
        # def f(root):
        #     if not root: return []
        #     return f(root.left) + [root.val] + f(root.right)
        # self.pointer = f(root)
        # self.cur = 0
        # self.len = len(self.pointer)
        self.stack = []
        self.push(root)

    def next(self) -> int:
        # v = self.pointer[self.cur]
        # self.cur += 1
        # return v
        if self.stack:
            v = self.stack.pop()
            self.push(v.right)
            return v.val
        return -1

    def push(self, node):
        while node:
            self.stack.append(node)
            node = node.left


    def hasNext(self) -> bool:
        return bool(self.stack)
        # return not self.cur == self.len
        

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()