def subsetXORSum(nums):

    def helper(nums,level,CurNum):

        if level == len(nums):
            return CurNum

        include = helper(nums,level+1, CurNum ^ nums[level])
        exclude = helper(nums,level+1, CurNum)

        return include + exclude

    return helper(nums,0,0)


nums= [5,1,6]
print(subsetXORSum(nums))