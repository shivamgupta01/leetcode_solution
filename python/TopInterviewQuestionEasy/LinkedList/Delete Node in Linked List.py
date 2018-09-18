# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

# Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, the linked list should become 1 -> 2 -> 4 after calling your function.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):

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