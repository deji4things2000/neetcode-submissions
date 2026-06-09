# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = []
        cur = head

        while cur:
            if cur.val != val:
                res.append(cur.val)
            cur = cur.next
        
        if not res:
            return None
        
        head = ListNode(res[0])
        cur = head

        for v in res[1:]:
            cur.next = ListNode(v)
            cur = cur.next
        return head

        

        