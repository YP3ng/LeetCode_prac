class Solution:
    def minFallingPathSum(self, matrix):
        # Get the size n
        n = len(matrix)
        # Copy input to update cell values throughtout the process
        grid = matrix

        # Start from second row
        for i in range(1, n):
            for j in range(n):

                # Cost from top left(i-1, j-1), check for boundaries
                if j-1 < 0:
                    left = float('inf')
                else:
                    left = grid[i-1][j-1]

                # Cost from top middle(i-1, j), don't need to check boundaries
                middle = grid[i-1][j]

                # Cost from top right(i-1, j+1), check for boundaries
                if j+1 > n-1:
                    right = float('inf')
                else:
                    right = grid[i-1][j+1]

                # Choose the min cost path and update current cell value
                grid[i][j] = grid[i][j] + min(left, middle, right)

        return min(grid[n-1])


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