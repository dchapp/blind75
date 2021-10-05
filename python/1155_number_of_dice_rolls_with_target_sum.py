
def gridprint(grid):
    for row in grid:
        print(row)

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
        Seems vaugely knapsack-like, so lets try 2D tabular DP
        """
        dp = [[0]*target for _ in range(d)]
        
        for i in range(min(f, target)):
            dp[0][i] = 1
            
        for i in range(d):    
            dp[i][i] = 1
        
        #gridprint(dp)
        
        for i in range(1, d):
            for j in range(i+1, target):
                curr_num_dice = i+1
                curr_target = j+1
                ways = 0
                #print(f"current target {curr_target}, current number of dice {curr_num_dice}")
                #gridprint(dp)
                for face_val in range(1, f+1):
                    next_target = curr_target - face_val
                    if next_target > 0:
                        res = dp[curr_num_dice-2][next_target-1]
                        #print(f"If current die rolls {face_val}, number of ways to make remaining {next_target} with remaining {curr_num_dice-1} dice is {res}")
                        ways += res
                #print(f"{ways} ways to make {curr_target} with {curr_num_dice} {f}-sided dice")
                dp[i][j] = ways % ((10**9) + 7)
                
        
        #gridprint(dp)
        
        return dp[-1][-1]
