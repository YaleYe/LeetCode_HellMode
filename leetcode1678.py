def interpret(command):

    string = ""

    index = 0
    while index <= len(command)-1:
        if command[index] == "G":
            string += "G"

            index += 1
        elif command[index] == "(":
            if command[index+1:index+3] == "al":
                string += "al"
                index += 4
            else:
                string += "o"
                index += 2
        else:
            return string



x = "G()()()()(al)"
interpret(x)