class Solution:
    def plusOne(self, digits):
        
        digits[-1] = digits[-1] + 1
        checker = 0
        
        for i in reversed(range(len(digits))):          
            if 10 - digits[i] == 0:
                digits[i] = 0
                if i - 1 < 0:
                    digits.insert(0,1)
                else:
                    digits[i-1] += 1
                    checker = 1
            else:
                checker = 0
            
        
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