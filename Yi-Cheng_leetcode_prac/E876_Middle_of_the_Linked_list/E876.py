# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head):
        cur = head
        count = 0

        while cur:
            count += 1
            if cur.next == None:
                break
            cur = cur.next

        if count % 2 != 0:
            recur = ((count - 1) / 2)
            res = head
            for i in range(int(recur)):
                res = res.next
            return res
        else:
            recur = (count / 2)
            res = head
            for i in range(int(recur)):
                res = res.next
            return res