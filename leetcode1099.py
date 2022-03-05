def twoSumLessThanK(nums,k):
    nums.sort()
    i = 0
    j = len(nums)-1
    ret = 0
    while i < j:
        if nums[i] + nums[j] >= k:
            j -= 1

        else:
            if nums[i] + nums[j] > ret:
                ret = nums[i]+nums[j]
            i += 1

    if ret == 0:
        return -1

    return ret

nums = [254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944]
k = 200

print(twoSumLessThanK(nums,k))