# 199. Binary Tree Right Side View

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root: return []
        q = deque([root])
        ans = []
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == 0:
                    ans.append(node.val)
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return ans



        