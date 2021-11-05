def areNumbersAscending(s):
    allItem = s.split()
    nums = []
    for item in allItem:
        if item.isdigit():
            if len(nums) == 0:
                nums.append(int(item))
            else:
                if nums[-1] >= int(item):
                    return False
                nums.append(int(item))
    return True

s = "4 5 11 26 12"
ans = areNumbersAscending(s)
print(ans)

