class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        else:
            max_products = [0]*(n+1)
            for i in range(1,5):
                max_products[i] = i
            #print(max_products)    
            for i in range(5, n+1):
                candidates = []
                for j in range(1, i-1):
                    remainder = i-j
                    #print(f"remainder: {remainder}, dp[j] = {max_products[j]}")
                    candidates.append(remainder * max_products[j])
                #print(candidates)    
                max_products[i] = max(candidates)
            return max_products[-1]
