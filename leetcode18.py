def fourSum(nums, k):
    nums.sort()

    containList = set()
    answer = []
    for point1 in range(0,len(nums)-3):
        for point4 in reversed(range(len(nums))):
            print(point4)
            leftpoint = point1 + 1
            rightpoint = point4 - 1

            while leftpoint < rightpoint:
                print(leftpoint)
                val = nums[point1] + nums[leftpoint] + nums[rightpoint] + nums[point4]
                if val == k:
                    if str(nums[point1])+"_"+str(nums[leftpoint])+"_"+str(nums[rightpoint])+"_"+str(nums[point4]) not in containList:
                        containList.add(str(nums[point1])+"_"+str(nums[leftpoint])+"_"+str(nums[rightpoint])+"_"+str(nums[point4]))
                        answer.append([nums[point1],nums[leftpoint], nums[rightpoint],nums[point4]])
                    leftpoint += 1
                elif val > k:
                    rightpoint -= 1
                elif val < k:
                    leftpoint += 1
    return answer

nums = [1,0,-1,0,-2,2]
target = 0
ans = fourSum(nums,target)
print(ans)