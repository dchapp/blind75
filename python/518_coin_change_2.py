
def brute_force(amount: int, coins: List[int]) -> int:
    
    ways = set()
    
    def worker(amount, coins, idx, choices):
        for i in range(idx, len(coins)):
            current_coin = coins[i]
            remaining = amount - current_coin
            updated_choices = list(choices)
            updated_choices.append(current_coin)
            if remaining == 0:
                ways.add(tuple(sorted(updated_choices)))
            elif remaining > 0:
                worker(remaining, coins, i, updated_choices)
        
    worker(amount, coins, 0, [])
    
    return len(ways)
    

def brute_force_2(amount: int, coins: List[int]) -> int:
    
    def worker(amount, coins, idx):
        ways = 0
        for i in range(idx, len(coins)):
            current_coin = coins[i]
            remainder = amount - current_coin
            if remainder == 0:
                ways += 1
            elif remainder > 0:
                ways += worker(remainder, coins, i)
        return ways
            
    return worker(amount, coins, 0) 
    
    
    
def memoized_recursive(amount: int, coins: List[int]) -> int:
    # Mapping from pair (amount, coin_idx) -> ways
    memo = {}
    
    def worker(amount, coins, idx):
        ways = 0
        for i in range(idx, len(coins)):
            current_coin = coins[i]
            remainder = amount - current_coin
            if remainder == 0:
                ways += 1
            elif remainder > 0:
                key = (remainder, i)
                if key not in memo:
                    memo[key] = worker(remainder, coins, i)
                ways += memo[key]
        return ways
            
    return worker(amount, coins, 0) 
    
           
def tabular_dp(amount: int, coins: List[int]) -> int:
    pass
    


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Brute force:
        - Create a tree where leaf nodes are combinations of coins that add to amount
        - Avoid double-counting combinations
        """
        
        if amount == 0:
            return 1

        return memoized_recursive(amount, coins)
