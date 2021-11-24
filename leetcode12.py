def intToRoman(num):
    dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        40: "XL",
        90: "XC",
        400: "CD",
        900: "CM",
        4: "IV",
        9: "IX",
        1000: "M",
    }
    divider = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    index = 0
    letter = ""
    while index != len(divider):
        counter = num // divider[index]
        if counter != 0:
            letter += counter * dict[divider[index]]
        num = num % divider[index]
        index += 1

    return letter

num = 58
x = intToRoman(num)
print(x)

