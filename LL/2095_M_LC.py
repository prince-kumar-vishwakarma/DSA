# 2095. Delete the Middle Node of a Linked List

class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if not head.next: return None
        slow = head
        fast = head.next
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head