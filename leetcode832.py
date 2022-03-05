def flipAndInvertImage(image):
    ret = []
    for i in image:
        temp = i[::-1]
        index = 0
        while index <= len(temp)-1:
            if temp[index] == 1:
                temp[index] = 0
                index += 1
            else:
                temp[index] = 1
                index += 1
        ret.append(temp)

    print(ret)

image = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]

flipAndInvertImage(image)