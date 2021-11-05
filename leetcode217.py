def containsDuplicate(nums):
    uniqluList = set()
    for num in nums:
        if num not in uniqluList:
            uniqluList.add(num)
        else:
            return True
    return False

nums = [1]

x = containsDuplicate(nums)
print(x)