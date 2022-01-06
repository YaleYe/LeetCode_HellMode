def combinationSum(candidates, target):

    ans = []

    def dfs(index, current):

        if sum(current) == target:
            ans.append(current.copy())
            return
        if sum(current) > target or index >= len(candidates):
            return

        current.append(candidates[index])

        dfs(index, current)
        current.pop()

        dfs(index+1,current)

    dfs(0,[])

    print(ans)


candidates = [2, 3, 5]
target = 8

combinationSum(candidates,target)