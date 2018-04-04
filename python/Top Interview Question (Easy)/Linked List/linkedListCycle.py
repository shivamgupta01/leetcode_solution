import python_topics.singlylinkedlist

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        d = {}
        d[head] = "In Dictionary"
        cur = head
        while cur:
            if cur.next in d:
                return True
            else:
                d[cur.next] = "In Dictionary"
            cur = cur.next
        return False


if __name__ == '__main__':
    s = Solution()

    mylist1 = python_topics.singlylinkedlist.linked_list()
    mylist1.addElement(1)
    mylist1.addElement(2)
    mylist1.addElement(3)
    mylist1.cycleLinkedList()
    print "solution : " + str(s.hasCycle(head=mylist1.head))







