'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) :

        # Linked list version
        if list1 == None: return list2
        if list2 == None: return list1
        if list1 == list2 == None: return None
        
        res = cur = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        return res.next

        # List version
        # len_a = len(list1)
        # len_b = len(list2)
        
        # if len_a == 0 and len_b == 0: return []
        
        # if len_a == 0: return list2
        # if len_b == 0: return list1
        
        # j = 0
        # res = []
        
        # for i in range(len_a):
            
        #     if j == len_b:
        #         for ele in list1[i:]:
        #             res.append(ele)
        #         break
            
        #     if list1[i] <= list2[j]:
        #         res.append(list1[i])
        #         res.append(list2[j])
        #     else:
        #         res.append(list2[j])
        #         res.append(list1[i])
                
            
        #     j += 1
        # return res

if __name__ == "__main__":

    s1 = Solution()

    list1 = [1,2,4]
    list2 = [1,3,4]
    # [1,1,2,3,4,4]
    print(s1.mergeTwoLists(list1, list2))