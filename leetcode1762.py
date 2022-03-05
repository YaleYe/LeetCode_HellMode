def findBuildings(heights):

    index = len(heights)-1
    max = 0
    answer = []
    while index >= 0:

        if heights[index] > max:
            answer.append(index)
            max = heights[index]
        index -= 1

    print(answer[::-1])

height = [1,3,2,4]
findBuildings(height)
