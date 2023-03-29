#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;


// ----------------------------------------------------------
// ----------------------------------------------------------
// LeetCode Problem Description
//  See https://leetcode.com/problems/reducing-dishes/description/

// My work on LeetCode
class Solution {
public:
    int maxSatisfaction(vector<int>& satisfaction) {
        sort(satisfaction.begin(), satisfaction.end(), [](auto& left, auto& right){
            return left >= right;
        });
        // Use Dynamic Programming
        if(satisfaction[0] <= 0) return 0;
        int ans = 0;
        int sum = 0;
        for(auto num : satisfaction){
            int deltaAns = num + sum;
            if(deltaAns <= 0) return ans;
            ans += deltaAns;
            sum += num;
        }
        return ans;

    }
};
// ----------------------------------------------------------
// ----------------------------------------------------------
//
int main(int argc, char **argv){
    Solution slnClass;
    // LeetCode generates test cases for me, but I need to create them manually here:
    std::vector<int> satisfaction = {-5,10,2,3,22,-10,-2,0,0,1};
    //  Sort dishes from smallest to largest and include all dishes in this case to get the max value, 328
    //  (Hence, ans should be 328)
    // Run the test case
    int ans = slnClass.maxSatisfaction(satisfaction);
    // Report the answer
    std::cout << "The answer is " << ans << "\n";
    return 0;
}
