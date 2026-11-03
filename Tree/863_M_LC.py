# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                parent[node.left.val] = node
                queue.append(node.left)
            if node.right:
                parent[node.right.val] = node
                queue.append(node.right)
        queue = deque([target])
        visited = {target.val}
        while k and queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left and node.left.val not in visited:
                    visited.add(node.left.val)
                    queue.append(node.left)
                if node.right and node.right.val not in visited:
                    visited.add(node.right.val)
                    queue.append(node.right)
                if node.val in parent and parent[node.val].val not in visited:
                    visited.add(parent[node.val].val)
                    queue.append(parent[node.val])
            k -= 1
        
        return [node.val for node in queue]


        