# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Build reversed copy using dummy
        dummy = ListNode(0)
        cur = head
        while cur:
            node = ListNode(cur.val)
            node.next = dummy.next
            dummy.next = node
            cur = cur.next

        # Compare original list with reversed copy
        p1, p2 = head, dummy.next
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True

