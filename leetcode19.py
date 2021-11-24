class Node:
    def __init__(self, new_data,next=None):
        self.data = new_data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # createNode and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next


    def printList(self):
        tmp_head = self.head
        while (tmp_head != None):
            print(tmp_head.data, end=' ')
            tmp_head = tmp_head.next


# Driver Code
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print("Created Linked list is:")
llist.printList()
llist.deleteNode(3)
print("\nLinked List after Deletion is:")
llist.printList()
