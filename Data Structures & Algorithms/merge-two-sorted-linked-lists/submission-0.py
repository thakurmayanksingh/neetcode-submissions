# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Step-1) Dummy Node Creation
        dummy = ListNode()
        tail = dummy
        # Step-2) Add tail values accordingly
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # Step-3) Handling the leftovers
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next