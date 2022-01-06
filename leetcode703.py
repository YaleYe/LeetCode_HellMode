from collections import deque
class KthLargest:

    def __init__(self, k,nums):
        self.k = k
        nums.sort(rev)


    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        print(self.nums)

        return self.nums[self.k]


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
kthLargest.add(5)
kthLargest.add(10)
kthLargest.add(9)
kthLargest.add(4)