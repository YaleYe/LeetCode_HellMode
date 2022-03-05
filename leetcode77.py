def combine(n,k):

    array = [i for i in range(1,n+1)]
    answer = []

    def dfs(index, curArray):
        if len(curArray) == k and curArray not in answer:
            answer.append(curArray.copy())

        if index > len(array)-1:
            return
        else:
            curArray.append(array[index])
            dfs(index+1,curArray)
            curArray.pop()
            dfs(index+1,curArray)

    dfs(0, [])
    print(answer)

combine(1,1)


