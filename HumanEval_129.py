def minPath(grid, k):
    """
    Finds the minimum-sum path of length k in an n×n grid.

    Args:
        grid (list of list of int): A 2D list representing the n×n grid.
        k (int): The length of the path to find.

    Returns:
        int: The minimum sum of a path of length k, or -1 if no such path exists.
    """
    n = len(grid)
    if k < 1 or k > n * n:
        return -1

    dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
    dp[0][0][1] = grid[0][0]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for length in range(1, k):
        for i in range(n):
            for j in range(n):
                if dp[i][j][length] < float('inf'):
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            dp[ni][nj][length + 1] = min(dp[ni][nj][length + 1], dp[i][j][length] + grid[ni][nj])

    min_sum = float('inf')
    for i in range(n):
        for j in range(n):
            min_sum = min(min_sum, dp[i][j][k])

    return min_sum if min_sum < float('inf') else -1
