def numberOfDays(year,month):

    if month in [1,3,5,7,8,10,12]:
        return 31

    if month in [4,6,9,11]:
        return 30

    else:
        if year % 4 == 0 and year %100 != 0 or year % 400 == 0:
            return 29
        else:
            return 28


print(numberOfDays(1200,2))