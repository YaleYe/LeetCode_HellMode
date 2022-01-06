def searchRange(nums, target):
    low = 0
    high = len(nums)
    recorder = []
    ans = []
    while low < high:
        mid = int((low+high)/2)
        # if its in mid

        if nums[mid] == target:
            if nums[mid-1] != target:
                ans.append(mid)
                low = high
            else:
                high = mid + 1

    low = 0
    high = len(nums)
    while low < high:
        mid = int((low+high)/2)
        # if its in mid
        if nums[mid] == target:
            if nums[mid+1] != target:
                ans.append(mid)
                low = high
            else:
                low = mid - 1

    if(ans):
        return ans
    else:
        return [-1,-1]

nums = [5,7,7,8,8,10]
target = 6
print(searchRange(nums,target))