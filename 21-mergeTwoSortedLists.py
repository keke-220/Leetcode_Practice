# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        
        head = ListNode()
        cur = head
        
        while p1 and p2:

            
            cur.next = ListNode()
            cur = cur.next
            if p1.val <= p2.val:
                cur.val = p1.val
                p1 = p1.next
            else:
                cur.val = p2.val
                p2 = p2.next
        print p1
        print p2
    
        if p1 != None:
            cur.next = p1
        if p2 != None:
            cur.next = p2

        return head.next
