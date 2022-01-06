def summaryRanges(nums):
    ret = []

    index = 1
    recorder = [nums[0]]
    while index <= len(nums) - 1:

        if recorder[-1] + 1 != nums[index]:
            if len(recorder) == 1:
                ret.append(str(recorder[0]))
                recorder = [nums[index]]
                index += 1
            else:
                string = str(recorder[0]) + "->" + str(recorder[-1])
                ret.append(string)
                recorder = [nums[index]]
                index += 1
        else:
            recorder.append(nums[index])
            index += 1
    print(recorder)

    if len(recorder) == 1:
        ret.append(str(recorder[0]))
    else:
        string = str(recorder[0]) + "->" + str(recorder[-1])
        ret.append(string)
    print(ret)


nums = [0,2,3,4,6,8,9]

summaryRanges(nums)
