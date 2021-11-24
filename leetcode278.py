class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        mid = 0
        while left <= right:
            mid = int((left + right) / 2)
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            if isBadVersion(mid):
                right = mid - 1
            if not isBadVersion(mid):
                left = mid + 1

