# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return head

        temp = head.next
        prev = head

        while temp != None:
            if temp.val == prev.val:
                prev.next = temp.next
                temp.next = None
                temp = prev.next
            else:
                temp = temp.next
                prev = prev.next
        return head

        