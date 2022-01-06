def subsets(nums):

    answer = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            answer.append(subset.copy())
            return

        # add left
        subset.append(nums[i])
        dfs(i+1)

        # add right
        subset.pop()
        dfs(i+1)


    dfs(0)
    return answer

num = [1,2,3]

print(subsets(num))