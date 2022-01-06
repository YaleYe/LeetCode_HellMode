def insection(nums1,nums2):

    dic = {

    }
    for num in nums1:
        if num not in dic:
            dic[num] = 1

    ans = set()

    for num in nums2:
        if num in dic.keys():
            ans.add(num)


    return list(ans)



nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

print(insection(nums1,nums2))