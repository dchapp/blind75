/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr) {
            return false;
        }
        return hash_table(head);
    }
private:
    
    bool hash_table(ListNode* head) {
        std::unordered_set<ListNode*> visited;
        while (head != nullptr) {
            const auto search = visited.find(head);
            if (search == visited.end()) {
                visited.insert(head);
            } else {
                return true;
            }
            head = head->next;
        }
        return false;
    }

    bool fast_slow_ptrs(ListNode* head) {
        auto slow = head;
        auto fast = head->next;
        while (slow != fast) {
            if (fast == nullptr || fast->next == nullptr) {
                return false;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        return true;
    }
};
