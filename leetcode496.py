def nextGreaterElement(nums1,num2):
    dic = {

    }
    index = 0

    while index <= len(num2) - 1:
        num = num2[index]
        tempIndex = index + 1
        while tempIndex <= len(num2) -1:
            if num2[tempIndex] > num:
                dic[num] = num2[tempIndex]
                break
            tempIndex += 1

            dic[num] = -1

        index += 1

    answer = []
    print(dic)
    print(dic[1])

    for num in nums1:
        if num not in dic:
            answer.append(-1)
        else:
            number = dic[num]
            answer.append(number)
    print(answer)


nums1 = [2,4]
nums2 = [1,2,3,4]
nextGreaterElement(nums1,nums2)

