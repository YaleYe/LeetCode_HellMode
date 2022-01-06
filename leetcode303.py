nums = [1,2,3]

nums2 = [0]

for num in nums:
    nums2.append(nums2[-1]+num)

print(nums2)
