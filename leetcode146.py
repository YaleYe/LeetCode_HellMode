class Node():
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            #print("key existed, get value")
            node = self.dict[key]
            self.delete(node)
            #print("added"+ str(node.value))
            self.add(node)

            print(self.dict.keys())
            return node.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            #check if node exist
            #print("key exist, update")
            node = self.dict[key]
            self.delete(node)
            node.value = value
            self.add(node)
        else:
            node = self.tail.prev
            #print("full capacity, remove noce"+str(node.value) )
            if len(self.dict) >= self.capacity:
                self.removeFromTail()

            newNode = Node(key,value)
            self.add(newNode)
            self.dict[key] = newNode
        print(self.dict.keys())



    def delete(self,node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def add(self,node):
        secondNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = secondNode
        node.next.prev = node

    def removeFromTail(self):
        if len(self.dict) == 0:
            return
        else:
            tailNode = self.tail.prev
            del self.dict[tailNode.key]
            self.delete(tailNode)






# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# ob j.put(key,value)
lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)   # return -1 (not found)
lRUCache.get(3)  # return 3
lRUCache.get(4) # return 4