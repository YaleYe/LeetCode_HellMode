import random
class Solution:

    def __init__(self, nums):
        self.original = nums

    def reset(self):
        print(self.original)
        return self.original

    def shuffle(self):
        newList = [self.original[i] for i in range(0,len(self.original))]
        random.shuffle(newList)
        return newList

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

so = Solution([1,2,3])
so.shuffle()
so.reset()
