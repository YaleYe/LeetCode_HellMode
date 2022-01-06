import collections


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.list = collections.deque([])
        self.capacity = capacity
        self.holding = collections.deque([])
        self.dequeNum = 0

    def enqueue(self, element: int) -> None:

        if self.dequeNum > 0:
            self.holding.append(element)
            self.dequeNum -= 1
            # if list is empty then nothing in holding
            if len(self.list) == 0:
                return self.holding.popleft()
            else:
                ans = self.list.popleft()
                if len(self.holding) > 0:
                    self.list.append(self.holding.popleft())
        else:
            # no deque
            if len(self.list) < self.capacity:
                self.list.append(element)
            else:
                self.holding.append(element)


    def dequeue(self) -> int:
        if len(self.list) != 0:
            ret = self.list.popleft()
            if len(self.holding) != 0:
                self.list.append(self.holding.popleft())
            return ret
        else:
            self.dequeNum += 1

    def size(self) -> int:
        return len(self.list)
