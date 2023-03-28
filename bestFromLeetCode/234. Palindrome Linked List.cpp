#include <iostream>
#include <vector>
using namespace std;


// ----------------------------------------------------------
// ----------------------------------------------------------
// LeetCode Problem Description
//  See https://leetcode.com/problems/palindrome-linked-list/

// From LeetCode:
// --------------
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// My work on LeetCode
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        // Construct the number
        vector<unsigned short> num;
        while(head != NULL){
            num.push_back(head->val);
            head = head->next;
        }
        //for(auto n : num) cout << n;
        // Check if the number is a palindrome
        for(int i = 0; i < num.size()/2; i++){
            if(num[i] != num[num.size()-i-1]) return false;
        }
        return true;
    }
};
// ----------------------------------------------------------
// ----------------------------------------------------------
//
int main(int argc, char **argv){
    Solution slnClass;
    // LeetCode generates test cases for me, but I need to create them manually here:
    ListNode* head = new ListNode(5);
    ListNode* n2 = new ListNode(3);
    head->next = n2;
    ListNode* n3 = new ListNode(5);
    n2->next = n3;

    // Run the test case
    bool ans = slnClass.isPalindrome(head);
    // Report the answer
    if(ans) std::cout << "head is a palindrome!\n";
    else std::cout << "head is NOT a palindrome!\n";
    return 0;
}
