def merge(num1,m,num2,n):

    for num in num2:
        num1[m] = num
        m += 1

    num1.sort()
    return num1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1,m,nums2,n))