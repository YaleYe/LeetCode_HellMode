def canBeEqual(target,arr):
    if sorted(target) == sorted(arr):
        return True

    return False


target = [1,2,3,4]
arr = [2,4,1,3]
print(canBeEqual(target,arr))