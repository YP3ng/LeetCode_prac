class Solution:
    def plusOne(self, digits):
        
        # Add 1 to the last int
        digits[-1] = digits[-1] + 1
        
        # Backward looping
        for i in reversed(range(len(digits))):          
            if 10 - digits[i] == 0: # Num bigger than or equal to 10
                digits[i] = 0
                if i - 1 < 0: # Check if it is the first int in the list
                    digits.insert(0,1)
                else:
                    digits[i-1] += 1
            
        
        return digits

if __name__ == "__main__":

    s1 = Solution()

    # 1 2 4
    inputList = [1,2,3]
    print(s1.plusOne(inputList))

    # 1 0 0
    inputList = [9,9]
    print(s1.plusOne(inputList))

    # 1 0
    inputList = [9]
    print(s1.plusOne(inputList))