'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import singlylinkedlist

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists_dict = {}
        for i in lists:
            lists_dict[i] = True
        head = None
        while len(lists_dict) != 0:
            temp_dict = {}
            for l,value in lists_dict.items():
                if l == None:
                    # del lists_dict[l]
                    continue
                temp = l.data
                if temp not in temp_dict:
                    temp_dict[temp] = [l]
                else:
                    temp_dict[temp] == temp_dict[temp].append(l)
            if len(temp_dict) != 0:
                min_value = min(temp_dict)
            else:
                return head

            for i in temp_dict[min_value]:
                # print(min_value)
                pntr = head
                newNode = singlylinkedlist.Node(min_value)
                if head == None:
                    head = newNode
                else:
                    while pntr.next != None:
                        pntr = pntr.next
                    pntr.next =  newNode
                if i.next == None:
                    del lists_dict[i]
                else:
                    del lists_dict[i]
                    lists_dict[i.next] = True
        if len(lists_dict) == 0:
                return head
            # print(lists)
         
                
            
        
        
            


if __name__ == '__main__':

    s = Solution()
    l1 = singlylinkedlist.linked_list()
    l2 = singlylinkedlist.linked_list()
    l3 = singlylinkedlist.linked_list()
    l1.addElement(6)
    # l1.addElement(4)
    # l1.addElement(1)
    # l2.addElement(7)
    l2.addElement(3)
    # l2.addElement(1)
    # l3.addElement(5)
    l3.addElement(2)
    l3.addElement(1)
    # 1-4-6
    # 1-3-7
    pntr = s.mergeKLists([l1.head,l2.head,l3.head])
    while pntr != None:
        print(pntr.data)
        pntr = pntr.next  
        