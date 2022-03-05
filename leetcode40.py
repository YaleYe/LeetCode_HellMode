def combinationSum2(candidates,target):

    ret = []

    candidates.sort()
    def backtrack(index,curArr,curSum):

        if curSum > target:
            return
        else:
            if curSum == target and sorted(curArr) not in ret:
                ret.append(sorted(curArr.copy()))
                return
            if index > len(candidates)-1:
                return
            else:
                curArr.append(candidates[index])
                backtrack(index+1, curArr,curSum+candidates[index])
                curArr.pop()
                backtrack(index+1, curArr,curSum)


    backtrack(0,[],0)
    return ret

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combinationSum2(candidates,target))
