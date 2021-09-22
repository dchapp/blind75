    

    
def naive_recursive(costs, house_idx, allow):
    allowed_costs = [costs[house_idx][i] for i in allow]
    if house_idx == len(costs)-1:
        return min(allowed_costs)
    else:
        candidates = []
        next_house_idx = house_idx + 1
        for cost_idx in allow:
            cost = costs[house_idx][cost_idx]
            if cost_idx == 0:
                candidates.append(cost + naive_recursive(costs, next_house_idx, [1,2]))
            elif cost_idx == 1:
                candidates.append(cost + naive_recursive(costs, next_house_idx, [0,2]))
            else:
                candidates.append(cost + naive_recursive(costs, next_house_idx, [0,1]))
        return min(candidates)

class Solution:
    
    top_down_memo = {}
    
    def minCost(self, costs: List[List[int]]) -> int:
        #return naive_recursive(costs, 0, [0,1,2])
        self.top_down_memo = {}
        return self.top_down_memoized_recursive(costs, 0, [0,1,2])
            
            
    def top_down_memoized_recursive(self, costs, house_idx, allow):
        allowed_costs = [costs[house_idx][i] for i in allow]
        if house_idx == len(costs)-1:
            return min(allowed_costs)
        else:
            candidates = []
            next_house_idx = house_idx + 1
            for cost_idx in allow:
                cost = costs[house_idx][cost_idx]
                if cost_idx == 0:
                    key = (next_house_idx, 1, 2)
                    if key not in self.top_down_memo:
                        candidate = cost + self.top_down_memoized_recursive(costs, next_house_idx, [1,2])
                        self.top_down_memo[key] = candidate
                elif cost_idx == 1:
                    key = (next_house_idx, 0, 2)
                    if key not in self.top_down_memo:
                        candidate = cost + self.top_down_memoized_recursive(costs, next_house_idx, [0,2])
                        self.top_down_memo[key] = candidate
                else:
                    key = (next_house_idx, 0, 1)
                    if key not in self.top_down_memo:
                        candidate = cost + self.top_down_memoized_recursive(costs, next_house_idx, [0,1])
                        self.top_down_memo[key] = candidate
                candidates.append(self.top_down_memo[key])
            return min(candidates)
    
