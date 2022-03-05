def findDuplicate(nums):
    existed = set()

    for num in nums:
        if num not in existed:
            existed.add(num)
        else:
            return num