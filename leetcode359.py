class Logger:

    def __init__(self):
        self.dict = {

        }
        self.messageList = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messageList:
            self.messageList.add(message)
            self.dict[message] = timestamp
            return True

        else:
            timeGap = self.dict[message]
            self.dict[message] += 10
            if timeGap + 10 == timestamp:
                return True

            return False

