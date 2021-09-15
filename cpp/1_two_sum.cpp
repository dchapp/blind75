#include <unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        const auto n_nums{nums.size()};
        std::unordered_map<int, int> complements;
        std::vector<int> ans;
        for (int i=0; i<n_nums; ++i) {
            const auto search = complements.find(nums[i]);
            if (search != complements.end()) {
                if (i != search->second) {
                    ans.push_back(i);
                    ans.push_back(search->second);
                    return ans;
                }
            } else {
                complements[target - nums[i]] = i;
            }
        }
        return ans;
    }
};
