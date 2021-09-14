/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        std::array<ListNode*,30> nodes;
        auto curr_idx = 0;
        auto curr = head;
        while (curr != nullptr) {
            nodes[curr_idx] = curr;
            ++curr_idx;
            curr = curr->next;
        }
        --curr_idx;
        const auto remove_idx = curr_idx - n + 1;
        if (remove_idx == curr_idx) {
            if (remove_idx == 0) {
                head = nullptr;
            } else {
                nodes[remove_idx-1]->next = nullptr;
            }
        } else {
            if (remove_idx == 0) {
                head = nodes[1];
            }
            if (remove_idx > 0 && remove_idx < curr_idx) {
                auto lower_neighbor = nodes[remove_idx-1];
                auto upper_neighbor = nodes[remove_idx+1];
                lower_neighbor->next = upper_neighbor;
            }
        }
        return head;
    }
};
