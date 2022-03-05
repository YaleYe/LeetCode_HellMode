import collections


def majorityElements(nums):

    dict = collections.Counter(nums)

    for key in dict:
        if dict[key] >= len(nums)/2:
            return key

nums = [2,2,1,1,1,2,2]
print(majorityElements(nums))