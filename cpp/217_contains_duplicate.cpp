#include <unordered_set>


static auto x = [](){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return nullptr;
}();


class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;
        for (const auto& n : nums) {
            const auto search = seen.find(n);
            if (search != seen.end()) {
                return true;
            } else {
                seen.insert(n);
            }
        }
        return false;
    }
    
    
    bool construct_set(const std::vector<int>& nums) {
        std::unordered_set<int> set{nums.begin(), nums.end()};
        return set.size() < nums.size();
    }
    
    bool naive_set(const std::vector<int>& nums) {
        std::unordered_set<int> seen;
        for (const auto& n : nums) {
            const auto search = seen.find(n);
            if (search != seen.end()) {
                return true;
            } else {
                seen.insert(n);
            }
        }
        return false;
    }
};
