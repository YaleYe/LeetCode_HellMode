class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None



a = ListNode(2)
b = ListNode(2)
c = ListNode(3)

a.next = c
b.next = c



print(a.next==b.next)