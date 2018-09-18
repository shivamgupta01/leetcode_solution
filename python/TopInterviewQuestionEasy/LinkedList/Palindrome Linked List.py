# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import singlylinkedlist

class Solution:
    def isPalindrome(self, head):
        if head == None:
            return True
        temp = []
        pointer = head
        mid = head

        size = 1
        while pointer.next != None:
            pointer = pointer.next
            size +=1
        pointer = head
        if size %2 == 0 :
            for i in range(int(size / 2)):
                mid = mid.next
            # print(mid.data)
            # print(pointer.data)
        else:
            for i in range(int(size / 2)+1):
                mid = mid.next
            
        while mid != None:
            temp.append(mid.data)
            mid = mid.next
        for item in temp[::-1]:
            if pointer.data != item:
                return False
            pointer = pointer.next
        
        return True
        


if __name__ == '__main__':
    s = Solution()
    mylist1 = singlylinkedlist.linked_list()
    # mylist1.addElement(2)
    # mylist1.addElement(1)
    # mylist1.addElement(2)
    # mylist1.addElement(1)


    print(s.isPalindrome(mylist1.head))    
        