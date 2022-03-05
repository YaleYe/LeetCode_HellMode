def createTargetArray(nums,index):
    target = []

    i = 0
    while i <= len(nums)-1:
        target.insert(index[i],nums[i])
        i += 1

    print(target)


nums = [0,1,2,3,4]
index = [0,1,2,2,1]

createTargetArray(nums,index)