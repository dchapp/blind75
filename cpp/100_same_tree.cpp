#include <iostream>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        auto same_value{false};
        if (p != nullptr && q != nullptr) {
            if (p->val == q->val) {
                same_value = true;
            } else {
                return false;
            }
        } else if (p == nullptr && q == nullptr) {
            return true;
        } else {
            return false;
        }
        auto same_left_subtree = isSameTree(p->left, q->left);
        auto same_right_subtree = isSameTree(p->right, q->right);
        return same_value && same_left_subtree && same_right_subtree;
    }
};
