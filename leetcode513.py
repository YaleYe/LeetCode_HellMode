# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        if not root:
            return

        que = deque([root])

        ans = []
        while que:
            root = que.popleft()

            ans.append(root.val)

            if root.right:
                que.append(root.right)
            if root.left:
                que.append(root.left)

        return ans[-1]
