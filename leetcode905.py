def sortArrayByParity(nums):

    odd = []
    even = []

    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even+odd

nums=[1,2,3,4,5,6,8,10,6]
print(sortArrayByParity(nums))