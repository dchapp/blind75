
def top_down_naive(houses: List[int]) -> int:
    def worker(houses):
        n_houses = len(houses)
        if n_houses == 0:
            return 0
        elif n_houses == 1 or n_houses == 2:
            return max(houses)
        else:
            candidate_1 = houses[n_houses-1] + top_down_naive(houses[:-2])
            candidate_2 = houses[n_houses-2] + top_down_naive(houses[:-3])
            return max(candidate_1, candidate_2)
    return worker(houses)



def top_down_memoized(houses: List[int]) -> int:
    memo = {}
    def worker(houses):
        n_houses = len(houses)
        if n_houses == 0:
            return 0
        elif n_houses == 1 or n_houses == 2:
            return max(houses)
        else:
            candidate_1_idx = n_houses-2
            candidate_2_idx = n_houses-3
            if candidate_1_idx not in memo:
                subproblem = worker(houses[:-2])
                memo[candidate_1_idx] = subproblem
            if candidate_2_idx not in memo:
                subproblem = worker(houses[:-3])
                memo[candidate_2_idx] = subproblem
            candidate_1 = nums[n_houses-1] + memo[candidate_1_idx]
            candidate_2 = nums[n_houses-2] + memo[candidate_2_idx]
            return max(candidate_1, candidate_2)
    return worker(houses)


def linear_dp(houses: List[int]) -> int:
    n_houses = len(houses)
    dp = [0]*(n_houses+1)
    dp[n_houses-1] = houses[n_houses-1]
    for i in range(n_houses-2, -1, -1):
        candidate_1 = dp[i+1]
        candidate_2 = dp[i+2] + houses[i]
        dp[i] = max(candidate_1, candidate_2)
    return dp[0]
    

def space_optimized_dp(houses: List[int]) -> int:
    n_houses = len(houses)
    pred_1 = 0
    pred_2 = houses[n_houses-1]
    curr = None
    for i in range(n_houses-2, -1, -1):
        curr = max((pred_1 + houses[i]), pred_2)
        pred_1 = pred_2
        pred_2 = curr
    return pred_2
    

class Solution:
    def rob(self, nums: List[int]) -> int:
        return space_optimized_dp(nums)
