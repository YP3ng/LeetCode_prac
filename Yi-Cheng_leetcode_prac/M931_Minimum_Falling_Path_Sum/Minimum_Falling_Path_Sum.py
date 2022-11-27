class Solution:
    def minFallingPathSum(self, matrix):
        pass


def test(matrix):
    s = Solution()
    res = s.minFallingPathSum(matrix)
    return res


if __name__ == "__main__":

    # Test case 1
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    assert test(matrix) == 13

    # Test case 2
    matrix = [[-19,57],[-40,-5]]
    assert test(matrix) == -59