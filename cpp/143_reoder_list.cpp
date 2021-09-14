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
    
private:
     
    std::pair<ListNode*, ListNode*> last_pair(ListNode* head) {
        auto prev = head;
        while (head->next != nullptr) {
            prev = head;
            head = head->next;
        }
        return std::make_pair(prev,head);
    }
};
