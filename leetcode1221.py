def balancedString(s):
    owed = 0

    counter = 0

    for char in s:
        if char == "L":
            owed -= 1
            if owed == 0:
                counter += 1
        if char == "R":
            owed += 1
            if owed == 0:
                counter += 1

    print(counter)


s = "RLLLLRRRLR"
balancedString(s)