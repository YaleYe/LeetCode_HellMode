def longestConsecutie(nums):

    num = set(nums)
    maxLen = 0
    for i in nums:

        if (i-1) not in num:
            counter = 1
            while i+1 in num:
                i = i + 1
                counter += 1

            maxLen = max(counter,maxLen)
    print(maxLen)

nums = [0,3,7,2,5,8,4,6,0,1]
longestConsecutie(nums)