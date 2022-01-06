def sumOfUnique(nums):
    dic = {

    }

    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

    sum = 0
    for key in dic.keys():
        if dic[key] == 1:
            sum += key
    print(sum)
    return sum

nums = [1,2,3,4,5]
sumOfUnique(nums)