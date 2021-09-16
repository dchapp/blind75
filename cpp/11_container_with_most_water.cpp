class Solution {
public:
    int maxArea(vector<int>& height) {
        //return brute_force(height);
        return two_pointer(height);
    }
    
    int two_pointer(const std::vector<int>& heights) {
        auto head_idx{0};
        auto tail_idx{heights.size()-1};
        auto area{0};
        while (head_idx < tail_idx) {
            const auto curr_area = get_area(heights, head_idx, tail_idx);
            if (curr_area > area) {
                area = curr_area;
            }
            if (heights[head_idx] < heights[tail_idx]) {
                ++head_idx;
            } else {
                --tail_idx;
            }
        }
        return area;
    }
    
    int get_area(const std::vector<int>& heights, int head_idx, int tail_idx) {
        const auto curr_len = tail_idx - head_idx;
        const auto box_height = std::min(heights[head_idx], heights[tail_idx]);
        return curr_len * box_height;
    }
    
    int brute_force(const std::vector<int>& heights) {
        auto area{0};
        const auto n = heights.size();
        for (int i=0; i<n; ++i) {
            for (int j=0; j<n; ++j) {
                if (j > i) {
                    const auto lb_height = heights[i];
                    const auto ub_height = heights[j];
                    const auto len = j - i;
                    const auto curr_area = std::min(lb_height, ub_height) * len;
                    if (curr_area > area) {
                        area = curr_area;
                    }
                }
            }
        }
        return area;
    }
};
