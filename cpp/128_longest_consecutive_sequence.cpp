#include <unordered_set>
#include <iostream>
#include <iomanip>


class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> vals{nums.begin(), nums.end()};
        auto ans{0};
        for (auto x : vals) {
            auto pred_search = vals.find(x-1);
            if (pred_search == vals.end()) {
                auto curr = x;
                auto curr_seq_len = 1;
                while (vals.find(curr+1) != vals.end()) {
                    ++curr;
                    ++curr_seq_len;
                }
                if (curr_seq_len > ans) {
                    ans = curr_seq_len;
                }
            }
        }
        return ans;
    }
    
};
