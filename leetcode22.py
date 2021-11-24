def generateParenthesis(n):

    result = []

    def backTrack(left,right,string, n):

        if left < right:
            return


        # if length = n
        if left == right == n:
            result.append(string)

        # if left > 0

        if left < right:
            return

        if left < n:
            backTrack(left+1, right, string+"(", n)

        if right < n:
            backTrack(left, right+1, string+")", n)

    backTrack(0,0,"",n)
    return result



num = 3
ans = generateParenthesis(num)
print(ans)
