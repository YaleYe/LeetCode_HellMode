def heightChecker(heights):

    newHeight = sorted(heights)

    index = 0
    counter = 0
    while index <= len(heights) - 1:
        if newHeight[index] != heights[index]:
            counter += 1

        index += 1

    return counter