def reorderLogFiles(logs):

    digitLog = []
    letterLog = []
    for log in logs:
        if log.split()[1].isdigit():
            digitLog.append(log)
        else:
            letterLog.append(log)

    letterLog.sort(key=lambda x: x.split()[0])
    letterLog.sort(key=lambda x: x.split()[1:])
    print(digitLog)
    return letterLog + digitLog

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
# ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
print(reorderLogFiles(logs))