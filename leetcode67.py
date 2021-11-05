def addBinary(a,b):
    if a == "0" and b == "0":
        return "0"
    ans = ""
    counter = max(len(a),len(b))
    if len(a) >= len(b):
        b = ((len(a) - len(b))*"0") + b
    else:
        a = ((len(b) - len(a)) * "0") + a

    carry = 0

    for index in range(1,counter+1):
        res = int(a[-1*index]) + int(b[-1*index]) + carry
        print(res)
        if res == 3:
            carry = 1
            ans += "1"
        if res == 2:
            carry = 1
            ans += "0"
        if res == 1:
            carry = 0
            ans += "1"
        if res == 0:
            carry = 0
            ans += "0"
    if carry == 1:
        ans += "1"

    ans = ans[::-1]
    return ans






a = "100"
b = "110010"

ans = addBinary(a,b)

print(ans)