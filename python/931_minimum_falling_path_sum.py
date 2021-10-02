class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        dp = [[0]*n_cols for _ in range(n_rows)]
        dp[-1] = matrix[-1]
        
        for i in range(n_rows-2, -1, -1):
            for j in range(n_cols):
                curr_element = matrix[i][j]
                if j == 0:
                    # special case 1: right-diagonal and lower neighbors
                    right_diagonal_path = dp[i+1][j+1] + curr_element
                    lower_path = dp[i+1][j] + curr_element
                    dp[i][j] = min(right_diagonal_path, lower_path) 
                elif j == n_cols-1:
                    # special case 2: left-diagonal and lower neighbors
                    left_diagonal_path = dp[i+1][j-1] + curr_element
                    lower_path = dp[i+1][j] + curr_element
                    dp[i][j] = min(left_diagonal_path, lower_path) 
                else:
                    # general case: left-diagonal, lower, and right-diagonal neighbors
                    left_diagonal_path = dp[i+1][j-1] + curr_element
                    right_diagonal_path = dp[i+1][j+1] + curr_element
                    lower_path = dp[i+1][j] + curr_element
                    dp[i][j] = min([left_diagonal_path, right_diagonal_path, lower_path]) 
                    
        return min(dp[0])

