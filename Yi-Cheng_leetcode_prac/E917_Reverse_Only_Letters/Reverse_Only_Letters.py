class Solution:
    def reverseOnlyLetters(self, s):
        # pointers on left and right, move in and swap.
        # if it is pointing to not English char, move in again
        
        left = 0
        right = len(s) - 1
        res = list(s) # Since String is immutable, need to break into list first

        while (right > left):
            left_check = s[left].isalpha()
            right_check = s[right].isalpha()

            # Check if char is alpha
            if left_check == False:
                res[left] = s[left]
                left += 1
                continue

            if right_check == False:
                res[right] = s[right]
                right -= 1
                continue
            
            # Swap
            res[left] = s[right] 
            res[right] = s[left]

            # Move pointer
            left += 1
            right -= 1

        return ''.join(res)

if __name__ == "__main__":
    s1 = Solution()

    s = "Test1ng-Leet=code-Q!"
    # "Qedo1ct-eeLg=ntse-T!"
    print(s1.reverseOnlyLetters(s))