# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        prev = None
        if head == None:
            return head

        nextNode = head.next
        while nextNode:
            head.next = prev
            prev = head
            head = nextNode
            nextNode = nextNode.next
            temp = head.val
        head.next = prev

        return head