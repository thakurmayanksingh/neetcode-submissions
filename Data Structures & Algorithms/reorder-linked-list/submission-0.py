# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step-1) Find MID
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        list2 = slow.next
        slow.next = None
        list1 = head
        # Step-2) Reverse List 2
        prev = None
        cur = list2
        nextt = None
        while cur:
            nextt = cur.next
            cur.next = prev
            prev = cur
            cur = nextt
        list2 = prev
        # Step-3) mapping the pointers accordingly
        while list1 and list2:
            t1 = list1.next
            t2 = list2.next
            list1.next = list2
            list1 = t1
            list2.next = list1
            list2 = t2