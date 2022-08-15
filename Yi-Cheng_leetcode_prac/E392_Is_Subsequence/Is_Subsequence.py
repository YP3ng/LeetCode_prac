'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

class Solution:
    def isSubsequence(self, s, t) :
        
        j = 0

        if len(s) == 0:
            return True

        for i in range(len(t)):

            if s[j] == t[i]:
                j += 1

            if j == len(s): # To avoid index out of range
                return True
        
        
        return False


if __name__ == "__main__":
    s1 = Solution()

    s = "abc"
    t = "ahbgdc"
    # True
    print(s1.isSubsequence(s,t))

    s = "b"
    t = "abc"
    # True
    print(s1.isSubsequence(s,t))