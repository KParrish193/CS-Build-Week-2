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

        head = ListNode(0)
        pointer = head
        lessVal = 0
         
        while l1.next is not None or l2.next is not None:
            if l1.next is None:
                pointer = l2
                break
            elif l2.next is None:
                pointer = l1
                break
            else:
                if l1.val <= l2.val:
                    lessVal = l1.val
                    l1 = l1.next
                else:
                    lessVal = l2.val
                    l2 = l2.next
            newNode = ListNode(lessVal)
            pointer.next = newNode
            pointer = pointer.next

        return head.next