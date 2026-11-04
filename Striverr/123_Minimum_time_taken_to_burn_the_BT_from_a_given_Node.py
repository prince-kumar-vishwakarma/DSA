# 123. Minimum time taken to burn the BT from a given Node


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def timeToBurnTree(self, root, start):
        #your code goes here
        parent = {}
        queue = deque([root])
        start_node = None
        while queue:
            node = queue.popleft()
            if node.data == start: 
                start_node = node
            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        queue = deque([start_node])
        visited = {start_node}
        time = 0
        while queue:
            n = len(queue)
            burned = False
            for _ in range(n):
                node = queue.popleft()
                neighbours = [node.left, node.right, parent.get(node)]
                for neighbour in neighbours:
                    if neighbour and neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                        burned = True
            if burned: time += 1
        return time


