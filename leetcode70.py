def climbStairs(n):
    stack = []
    def backtrack(counter, n, stack):
        if counter == n:
            stack.append(1)
            return
        if counter < n:
            backtrack(counter+1, n,stack)
            backtrack(counter+2, n,stack)

    backtrack(0, n,stack)

    print(len(stack))

climbStairs(3)
