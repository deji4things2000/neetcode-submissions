# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # Step 1: Move fast ahead by n nodes
        while n>0:
            fast = fast.next
            n-=1


        # Step 2: Move both pointers until fast reaches the last node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next



        # Step 3: Remove the target node
        slow.next = slow.next.next


        return dummy.next

        