class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        que = deque([(root, 1)])

        while que:
            root, num = que.popleft()

            if not root.left and not root.right:
                return num
            if root.left:
                que.append((root.left, num + 1))
            if root.right:
                que.append((root.right, num + 1))

        return -1