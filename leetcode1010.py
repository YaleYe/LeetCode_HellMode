def numPairsDivisibleBy60(time):

    dp = [0]* 60
    ret = 0
    for t in time:
        reminder = t % 60
        target = 60 - reminder
        ret += dp[target]
        dp[reminder] += 1

    return ret


time = [30,20,150,100,40]

print(numPairsDivisibleBy60(time))