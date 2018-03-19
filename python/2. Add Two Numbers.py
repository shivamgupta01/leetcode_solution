"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""

class Node(object):

    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d

class Solution(object):


    def __init__(self, r=None):
        self.root = r
        self.size = 0

    def find(self, d):
        this_node = self.root
        while this_node:
            size = size +1

    def addTwoNumbers (self, l1,l2):
        this_node = l1.root
        while this_node:
            print this_node.get_data()
