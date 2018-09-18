# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        curr = head.next
        size = 1
        temp = head
        while curr:
            size += 1
            curr = curr.next

        # head.next.next.next.next.next.next = head.next.next.next.next.next.next.next
        x = size - n
        if size == 1:
            head = None
            return head
        elif x == 0:
            head = head.next
            return head
        while x > 1:
            temp = temp.next
            print x
            x = x - 1
        temp.next = temp.next.next
        return head

