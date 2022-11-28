class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # Solution 1: Swapping
        n = len(s)
        if n % 2 == 0:
            for i in range(int(n/2)):
                tmp = s[i]
                s[i] = s[len(s) - 1 - i]
                s[len(s) -1 -i] = tmp
        else:
            for i in range(int((n-1)/2)):
                tmp = s[i]
                s[i] = s[len(s) - 1 - i]
                s[len(s) -1 -i] = tmp

        # Solution 2: Two pointers
        # i, j = 0, len(s) -1
        # while i < j:
        #     s[i], s[j] = s[j], s[i]
        #     i += 1
        #     j -= 1


def test(input):
    s = Solution()
    s.reverseString(input)
    return input

if __name__ == "__main__":
    input = ["h","e","l","l","o"]
    assert ["o","l","l","e","h"] == test(input)

    input = ["H","a","n","n","a","h"]
    assert ["h","a","n","n","a","H"] == test(input)