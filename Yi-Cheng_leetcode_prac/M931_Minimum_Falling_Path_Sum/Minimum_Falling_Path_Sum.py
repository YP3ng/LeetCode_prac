class Solution:
    def minFallingPathSum(self, matrix):
        pass


def test():
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    s = Solution()
    res = s.minFallingPathSum(matrix)
    return res


if __name__ == "__main__":
    assert test() == 13