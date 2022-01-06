import collections


class MovingAverage:

    def __init__(self, size: int):
        self.list = collections.deque([])
        self.size = size

    def next(self, val: int) -> float:
        if len(self.list) == self.size -1:
            self.list.popleft()

        self.list.append(val)

        return sum(self.list)/ len(self.list)

