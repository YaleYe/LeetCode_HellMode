def fourSumCount(nums1,nums2,nums3,nums4):

    dict = {}

    for num in nums1:
        for num2 in nums2:
            key = 0 - num - num2

            if key not in dict:
                dict[key] = 1
            else:
                dict[key] += 1

    # 1,1
    # 0-2
    # -2
    count = 0
    for num in nums3:
        for num2 in nums4:
            key =  num+num2
            if key in dict.keys():
                count += dict[key]

    return count



nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]

print(fourSumCount(nums1,nums2,nums3,nums4))