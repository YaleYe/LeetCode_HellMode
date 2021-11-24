# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maximumAverageSubtree(self, root) -> float:
        self.maxNum = 0

        def helper(root) -> (int, int):
            if not root:
                return (0, 0)

            (leftVal, leftCount), (rightVal, rightCount) = helper(root.left), helper(root.right)

            totalVal = root.val + leftVal + rightVal
            totalCount = leftCount + rightCount + 1
            averageNum = totalVal / totalCount
            self.maxNum = max(self.maxNum, averageNum)
            return (totalCount, averageNum)

        helper(root)

        return self.maxNum

