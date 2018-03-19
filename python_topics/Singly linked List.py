class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def getval(self):
        return self.val

    def setval(self, val):
        self.val = val

    def getnext(self):
        return self.next

    def setnext(self, val):
        self.next = val


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self, val):
        newNode = Node(val, self.head)
        self.head = newNode
        self.size += 1
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.getnext()

    def delNode(self,val):
        curr = self.head
        while curr.val == val:
            self.head = curr.getnext()
            curr=self.head

        while curr:
            if curr.getnext()== None:
                return False
            elif curr.getnext().val == val:
                curr.setnext(curr.getnext().getnext())
                return True
            curr = curr.getnext()


    def delnthnode(self,head,n):
        # Definition for singly-linked list.
        # class ListNode(object):
        #     def __init__(self, x):
        #         self.val = x
        #         self.next = None

        temp = curr = head

        try:
            while n >= 0:
                temp = temp.next
                n = n - 1
        except:
            head = head.next
            return head

        while temp:
            temp = temp.next
            curr = curr.next
        curr.next = curr.next.next
        return head
    def reverseLinkedList(self, head):
        prev = None
        if head == None:
            return head

        nextNode = head.next

        while nextNode:
            head.next = prev
            prev = head
            head = nextNode
            nextNode = nextNode.next
        head.next = prev
        return head

        curr = self.head
        while curr:
            print curr.val
            curr = curr.getnext()



    def sortTwoList(self,head1,head2):
        print "hey"













myList = LinkedList()

print(myList.addNode(5))
print(myList.addNode(4))
print(myList.addNode(3))
print(myList.addNode(2))
print(myList.addNode(1))
(myList.reverseLinkedList(myList.head))


