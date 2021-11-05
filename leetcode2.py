# Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def addTwoNumbers(l1, l2):
    if not l1:
        return l2

    if not l2:
        return l1

    carry = 0
    addVal = (l1.val + l2.val + carry) % 10

    l3 = ListNode(addVal)

    carry = (l1.val + l2.val + carry) // 10
    cur = l3

    while l1.next and l2.next:
        l1 = l1.next
        l2 = l2.next
        addVal = (l1.val + l2.val + carry) % 10
        carry = (l1.val + l2.val + carry) // 10
        cur = ListNode(addVal)
        cur = cur.next

    while l1.next:
        l1 = l1.next
        addVal = (l1.val + carry) % 10
        carry = (l1.val + carry) // 10
        cur = ListNode(addVal)
        cur = cur.next

    while l2.next:
        l2 = l2.next
        addVal = (l1.val + carry) % 10
        carry = (l1.val + carry) // 10
        cur = ListNode(addVal)
        cur = cur.next

    if carry == 1:
        cur = ListNode(1)
        return l3

    return l3
