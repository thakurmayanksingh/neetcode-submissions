# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow = head
        # fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow==fast:
        #         return True
        # return False

        mp = {}
        cur = head
        while cur:
            if cur in mp:
                return True
            else:
                mp[cur] = 1
                cur = cur.next
        return False