# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        p1 = l1
        p2 = l2
        head = None
        tail = None
        
        if p1.val <= p2.val:
            head = p1
            tail = p1
            p1 = p1.next
            
        else:
            head = p2
            tail = p2
            p2 = p2.next
        
        while p1 and p2:          
            if p1.val <= p2.val:      
                tail.next = p1
                tail = p1
                p1 = p1.next
            else: 
                tail.next = p2
                tail = p2
                p2 = p2.next
    
        if p1 is None:
            tail.next = p2
        elif p2 is None:
            tail.next = p1
    
        return head
            
        