class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self,head=None):
        self.head = head

    def addElement(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total = total+1
            cur = cur.next
        return total

    # def printListItems(self):
    #     cur = self.head
    #     while cur:
    #         print cur.data
    #         cur = cur.next

    def cycleLinkedList(self):
        cur = self.head
        while cur:
            if cur.next == None:
                cur.next = self.head
                break
            cur = cur.next






