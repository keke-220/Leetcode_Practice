# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode((l1.val + l2.val)%10)
        ans = res
        c = (l1.val + l2.val) // 10
        while (l1.next != None or l2.next != None or c != 0):
            res.next = ListNode(0)
            res = res.next
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            sum = l1.next.val + l2.next.val + c
            if sum >= 10:
                c = 1
            else:
                c = 0
            res.val = sum % 10
            print(res.val)
            l1 = l1.next
            l2 = l2.next 

        return ans
