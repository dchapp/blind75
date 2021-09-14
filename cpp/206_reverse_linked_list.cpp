#include <stack>
#include <iostream>

//static int x = []() {
//  std::ios::sync_with_stdio(false);
//  std::cin.tie(nullptr);
//  return 0;
//}();

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
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) {
            return head;
        }
        return recursive(head);
    }
    
    
private:
    
    ListNode* recursive(ListNode* head) {
        // Base case: no next node, just return head
        if (head->next == nullptr || head->next == nullptr) {
            return head;
        } else {
            auto p = recursive(head->next);
            head->next->next = head;
            head->next = nullptr;
            return p;
        }
    }
    
    // 9ms 8.3MB / 7ms 8.4MB w/ untie
    ListNode* iterative(ListNode* head) {
        auto curr = head;
        ListNode* next = nullptr;
        ListNode* prev = nullptr;
        while (curr != nullptr) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
    
    // 4ms 8.4MB best -- highly variable timing, untie made much worse (14ms)
    ListNode* stack(ListNode* head) {
        std::stack<ListNode*> nodes;
        auto* curr = head;
        while (curr != nullptr) {
            nodes.push(curr);
            curr = curr->next;
        }
        auto* new_head = nodes.top();
        nodes.pop();
        curr = new_head;
        while (!nodes.empty()) {
            auto* next = nodes.top();
            nodes.pop();
            curr->next = next;
            curr = next;
        }
        curr->next = nullptr;
        return new_head;
    }
    
};
