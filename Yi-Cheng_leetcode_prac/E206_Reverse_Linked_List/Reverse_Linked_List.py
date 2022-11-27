#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        current = head
        prev = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev


if __name__ == "__main__":
    s = Solution()

    # [1,2,3, None]
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3

    # Get the result
    res = s.reverseList(n1)

    # Print out
    outcome = []
    while res:
        nxt = res.next
        outcome.append(res.val)
        res = nxt

        if res == None:
            outcome.append(None)


    print(outcome)