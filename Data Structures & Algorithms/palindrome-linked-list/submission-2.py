# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Build reversed copy using dummy
        res = []
        cur = head

        while cur:
            res.append(cur.val)
            cur = cur.next

        cur = head

        while cur:
            if cur.val != res.pop():
                return False
            cur = cur.next
        return True