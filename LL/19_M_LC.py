# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head or not head.next: return None
        length = 0
        temp = head
        while temp: 
            length += 1
            temp = temp.next
        k = length-n
        if k == 0: return head.next
        temp = head
        for _ in range(k-1):
            temp = temp.next
        temp.next = temp.next.next
        return head


