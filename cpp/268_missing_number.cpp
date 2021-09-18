class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // sum of 0 + 1 + 2 ... + n is n*(n+1)/2 
        auto n = nums.size();
        auto sum = std::accumulate(nums.begin(), nums.end(), 0);
        return (n*(n+1)/2) - sum;
    }
};
