class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        deq = deque([(root, 0)])
        val = []

        while deq:
            root, level = deq.popleft()

            if level >= len(val):
                val.append([])

            val[level].append(root.val)

            if root.left:
                deq.append((root.left, level + 1))

            if root.right:
                deq.append((root.right, level + 1))

        newAns = []

        for eachNumList in val:
            newAns.append(sum(eachNumList) / len(eachNumList))

        return newAns