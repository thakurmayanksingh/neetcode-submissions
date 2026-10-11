# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
            
        pos = size - n
        curPos = 0
        cur = head
        prev = None

        while cur:
            if curPos == pos:
                if prev is None:
                    return head.next
                else:
                    prev.next = cur.next
                    return head
            else:
                curPos += 1
                prev = cur
                cur = cur.next
        
        return head