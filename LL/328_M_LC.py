# 328. Odd Even Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next: return head
        oddS = head 
        evenS = head.next

        odd = oddS
        even = evenS
        isOdd = True
        temp = evenS.next

        while temp:
            if isOdd:
                odd.next = temp
                odd = odd.next
            else:
                even.next = temp
                even = even.next
            isOdd = not isOdd
            temp = temp.next
        even.next = None
        odd.next = evenS
        return oddS
            
        
        
        

        


        