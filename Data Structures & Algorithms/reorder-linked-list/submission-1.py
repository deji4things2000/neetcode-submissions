# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Step 1: Use fast and slow to determine midpoint
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Step 2: Divide the list into two at midpoint
        second = slow.next
        slow.next = None

        #Step 3: Reverse the second list
        prev = None
        cur = second

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        second = prev
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

        

