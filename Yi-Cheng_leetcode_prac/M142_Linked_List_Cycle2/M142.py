# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        fast, slow = head, head

        # Check for single val
        if (head == None
            or head.next == None):
            return None

        # Check if circle exist
        while (slow != None
                and fast != None
                and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # If pointers don't meet, return null
        if slow != fast:
            return None
        
        # Find the starting point of circle
        # Reset slow pointer
        slow = head

        # When slow meets fast, return the val
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

        