def subdomainVisits(cpdomains):
    dict = {}

    for domain in cpdomains:
        domainList = domain.split(" ")
        counter = int(domainList[0])
        subDomain = domainList[1].split(".")
        for index in range(len(subDomain),-1,-1):
            curDomain = '.'.join(subDomain[index:])
            if curDomain in dict:
                dict[curDomain] += counter
            else:
                dict[curDomain] = counter

    answer = []

    for key in dict:
        if key != "":
            addedString = str(dict[key])+" "+str(key)
            answer.append(addedString)

    print(answer)
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
subdomainVisits(cpdomains)
