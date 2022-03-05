import collections


class BrowserHistory:

    def __init__(self, homepage: str):
        self.visitedHistory = []
        self.future = []
        self.visit(homepage)

    def visit(self, url: str) -> None:
        self.visitedHistory.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        while steps >0 and len(self.visitedHistory) > 1:
            self.future.append(self.visitedHistory.pop())
            steps -= 1

        print(self.visitedHistory[-1])
        return self.visitedHistory[-1]


    def forward(self, steps: int) -> str:
        while steps >0 and len(self.future) > 0:
            self.visitedHistory.append(self.future.pop())
            steps -= 1

        print(self.visitedHistory[-1])
        return self.visitedHistory[-1]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


history = BrowserHistory("leetcode.com")
history.visit("google.com")
history.visit("facebook.com")
history.visit("youtube.com")
history.back(1)
history.back(1)
history.forward(1)
history.visit("linkedin")
history.forward(2)
history.back(2)
history.back(7)