def findValueAfterOperations(operations):
    initNum = 0

    for operation in operations:
        if operation in ["--X","X--"]:
            initNum -= 1

        else:
            initNum += 1

    return initNum



operations = ["--X","X++","X++"]
print(findValueAfterOperations(operations))