#include <algorithm>

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
    void reorderList(ListNode* head) {
        if (head->next == nullptr) {
            return;
        }
        iterative_linear_space(head);
    }
    
private:
    
    void iterative_linear_space(ListNode* head) {
        std::vector<ListNode*> first_half;
        std::vector<ListNode*> last_half;
        auto n_nodes{0};
        auto curr = head;
        while (curr != nullptr) {
            curr = curr->next;
            ++n_nodes;
        }
        curr = head;
        auto idx{0};
        while(curr != nullptr) {
            if (idx < n_nodes/2) {
                first_half.push_back(curr);
            } else {
                last_half.push_back(curr);
            }
            curr = curr->next;
            ++idx;
        }
        
        std::reverse(last_half.begin(), last_half.end());
        
        const auto n = std::max(first_half.size(), last_half.size());
        for (int i=0; i<n; ++i) {
            if (i < first_half.size()) {
                first_half[i]->next = last_half[i];
            }
            if (i+1 < first_half.size()) {
                last_half[i]->next = first_half[i+1];
            } else {
                if (i+1 < last_half.size()) {
                    last_half[i]->next = last_half[i+1];
                }
            }
        }
        last_half[last_half.size()-1]->next = nullptr;

        head = first_half[0];
    }
    
    
    void recursive_constant_space(ListNode* head) {
        if (head->next == nullptr || head->next->next == nullptr) {
            return;
        }
        
        auto [prev, last] = last_pair(head);
        prev->next = nullptr;
        auto new_head = head->next;
        head->next = last;
        last->next = new_head;
        reorderList(new_head);
    }
    
    
    std::pair<ListNode*, ListNode*> last_pair(ListNode* head) {
        auto prev = head;
        while (head->next != nullptr) {
            prev = head;
            head = head->next;
        }
        return std::make_pair(prev,head);
    }
};
