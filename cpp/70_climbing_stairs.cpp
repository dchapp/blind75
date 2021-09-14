class Solution {
public:
    int climbStairs(int n) {
        for (int i=0; i<memo.size(); ++i) {
            memo[i] = -1;
        }
        memo[0] = 1;
        memo[1] = 2;
        return worker(n);
    }
private:
    int worker(int n) {
        const auto idx = n-1;
        if (memo[idx] == -1) {
            const auto ans = worker(n-1) + worker(n-2);
            memo[idx] = ans;
        } 
        return memo[idx];
    }
    std::array<int, 45> memo; 
};
