def myAtoi(s):
    try:
        ans = s.split()[0]
        neg = 1
        if ans[0] == "-":
            neg = -1
            ans = ans[1:]
        if ans[0] == "+":
            ans = ans[1:]

        if ans[0] == "-" and ans[1] == "+":
            return 0
        res = ""

        index = 0
        while ans[index].isdigit() and index <= len(ans) -1:
            res += ans[index]
            index += 1
            if index == len(ans):
                break
        if int(res) * neg < -2147483648:
            return -2147483648
        if int(res) * neg > 2147483647:
            return 2147483647
        return int(res)*neg

    except:
        return 0



s =  "-+"
ans = myAtoi(s)
print(ans)