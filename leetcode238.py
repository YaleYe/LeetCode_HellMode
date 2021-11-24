def productExceptSelf(nums):

    preFix = [1] * (len(nums) + 1)
    postFix = [1] * (len(nums)+ 1)
    ans = []
    index = 1

    while index-1 < len(nums):
        preFix[index] *= preFix[index-1] * nums[index-1]
        postFix[-index-1] *= postFix[-index] * nums[-index]
        index += 1

    secondIndex = 0
    while secondIndex <= len(preFix)-2:
        ans.append(preFix[secondIndex]*postFix[secondIndex+1])
        secondIndex += 1



    print(preFix)
    print(postFix)
    print(ans)
nums = [1,2,3,4]
productExceptSelf(nums)