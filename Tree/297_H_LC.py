# 297. Serialize and Deserialize Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        queue = deque([root])
        code = ""
        while queue:
            node = queue.popleft()
            if node is None:
                code += "#,"
            else:
                code += f"{node.val},"
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
        return code
            


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "": return None
        arr = data.split(",")
        n = len(arr)
        root = TreeNode(int(arr[0]))
        i = 1
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if arr[i] == "#":
                node.left = None
            else:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1
            if arr[i] == "#":
                node.right = None
            else:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))