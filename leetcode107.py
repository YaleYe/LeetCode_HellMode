# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        deq = duque([(root, 0)])

        numList = []
        while deq:
            root, level = deq.popleft()

            if level >= len(numList):
                numList.append([])

            numList[level].append(root.val)

            if root.left:
                deq.append((root.left, level + 1))

            if root.right:
                deq.append((root.right, level + 1))

        return numList[::-1]