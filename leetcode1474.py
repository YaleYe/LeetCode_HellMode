def printList(list,m,n):

    index = 0
    ans = []

    m_switch = True
    n_switch = False

    while index <= len(list)-1:


        if m_switch:
            for i in list[index:index+m]:
                ans.append(i)
            index += m
            m_switch = False
            n_switch= True

        if n_switch:

            index += n
            m_switch = True
            n_switch = False


    print(ans)

head = [1,2,3,4,5,6,7,8,9,10,11]
m = 1
n = 3
printList(head,m,n)
