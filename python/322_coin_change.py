class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0
        for c in coins:
            if c < amount+1:
                dp[c] = 1
        for i in range(1, len(dp)):
            if i not in coins:
                candidates = []
                for c in coins:
                    new_amount = i-c
                    if new_amount > 0 and dp[i-c] != -1:
                        candidates.append(dp[i-c]+1)
                if len(candidates) > 0:        
                    dp[i] = min(candidates)
        #print(dp)        
        return dp[-1]
