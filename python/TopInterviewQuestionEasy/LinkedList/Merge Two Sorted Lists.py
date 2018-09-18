# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import singlylinkedlist

class Solution:
   
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """ 
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        head = None
        count = 0
        while (l1 != None) or  (l2 != None):
            count = count +1
            # print(count+1)
            if l1 == None:
                pntr = head
                while pntr.next != None:
                    pntr = pntr.next
                pntr.next = l2
                return head
            elif l2 == None:
                pntr = head
                while pntr.next != None:
                    pntr = pntr.next
                pntr.next = l1
                return head
            else:
                if l1.data >= l2.data:
                    newNode = singlylinkedlist.Node(l2.data)
                    l2 = l2.next
                else:
                    newNode = singlylinkedlist.Node(l1.data)
                    l1 = l1.next
                if head == None:
                    head = newNode
                else:
                    pntr = head
                    while(pntr.next!=None):
                        pntr = pntr.next
                    pntr.next = newNode
        return head

        

if __name__ == '__main__':
    s = Solution()
    l1 = singlylinkedlist.linked_list()
    l2 = singlylinkedlist.linked_list()
    l1.addElement(6)
    l1.addElement(4)
    l1.addElement(1)
    # l2.addElement(7)
    # l2.addElement(3)
    # l2.addElement(1)
    # 1-4-6
    # 1-3-7
    pntr = s.mergeTwoLists(l1.head,l2.head)
    while pntr != None:
        print(pntr.data)
        pntr = pntr.next  