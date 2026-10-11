# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prevNode = None
        # curNode = head
        # nextNode = None
        # while curNode:
        #     nextNode = curNode.next
        #     curNode.next = prevNode
        #     prevNode = curNode
        #     curNode = nextNode
        # return prevNode
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev