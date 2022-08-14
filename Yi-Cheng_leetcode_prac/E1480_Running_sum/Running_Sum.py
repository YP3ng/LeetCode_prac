class Solution:
    def runningSum(self, nums):
        
        prev = 0
        res = []
        
        for ele in nums:
            prev += ele
            res.append(prev)
            
        return res