# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Identify the midpoint
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Break the list into two points
        second = slow.next
        slow.next = None

        #Reverse the second list
        prev = None
        cur = second

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        second = prev

        #Now, for each index, join the corresponding node
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2






        