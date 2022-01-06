def intersect(num1,num2):

    dic = {

    }
    for num in num1:
        if num in dic.keys():
            dic[num] += 1
        else:
            dic[num] = 1

    ans = []
    for num in num2:
        if num in dic.keys() and dic[num] >= 1:
            ans.append(num)
            dic[num] -= 1

    return ans


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1,nums2))