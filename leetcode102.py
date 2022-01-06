# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        val = []
        # take root and level
        que = deque([(root, 0)])

        while que:
            root, level = que.popleft()

            # if the list is empty, create a list
            if len(val) <= level:
                val.append([])

            val[level].append(root.val)

            if root.left:
                que.append((root.left, level + 1))

            if root.right:
                que.append((root.right, level + 1))

        return val
