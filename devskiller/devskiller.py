class fizzBuzz():

    def __init__(self):
        self.dict = {
            3:"Fizz",
            5:"Buzz"
        }
        self.dividers = [3,5]

    def generateToken(self,divider,words):

        self.dict[divider] = words
        self.dividers.append(divider)
        self.dividers.sort()

    def output(self,number):

        ansList = []

        for x in range(1,number+1):
            curString = ""

            for divider in self.dividers:
                if x % divider == 0:
                    curString += self.dict[divider]

            if curString == "":
                curString = str(x)

            ansList.append(curString)

        return ansList


#fizz = fizzBuzz()
#print(fizz.output(10))

#fizz.generateToken(4,"forg")
#fizz.generateToken(13,"duck")
#fizz.generateToken(9,"chicken")
#print(fizz.output(13))

def advanced():

    ansList = []

    for x in range(-12,146):
        if x % 3 == x % 7 == x % 38 == 0:
            ansList.append("GZB")
        else:
            curString = ""
            if x % 3 == 0:
                curString += "F"
            if x % 7 == 0:
                curString += "B"
            if x % 38 == 0:
                curString += "Baz"
            if curString == "":
                ansList.append(str(x))
            else:
                ansList.append(curString)

    print(ansList)

advanced()
