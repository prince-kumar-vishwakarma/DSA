# 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        mini = float("inf")
        i = 2
        preVal = head.val
        temp = head.next
        first = 0
        lastCP = 0
        while temp.next:
            if preVal < temp.val > temp.next.val or preVal > temp.val < temp.next.val:
                if first:
                    mini = min(mini, i-lastCP)
                lastCP = i
                if not first: first = i
            i += 1
            preVal = temp.val
            temp = temp.next
        if first != lastCP:
            return [mini, lastCP-first]
        else:
            return [-1, -1]

        
        