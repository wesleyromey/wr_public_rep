##############################################################
# LeetCode Template
"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
"""

##############################################################
# Link to problem: https://leetcode.com/problems/sum-root-to-leaf-numbers/

##############################################################
# My LeetCode solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        def solve(root, ans: list, curDigits: str) -> None:
            curDigits += str(root.val)
            if root.left is None:
                if root.right:
                    solve(root.right, ans, curDigits)
                else:
                    ans.append(curDigits)
            else:
                solve(root.left, ans, curDigits)
                if root.right:
                    solve(root.right, ans, curDigits)
        ans = []
        curDigits = ""
        solve(root, ans, curDigits)
        res = 0
        for item in ans:
            res += int(item)
        return res

##############################################################
# Extra code needed to make the LeetCode Solution run
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def __main__():
    # First, create the test cases.
    #   NOTE that LeetCode generated most or all of the test cases for me
    root = TreeNode(5)
    root.left, root.right = TreeNode(2), TreeNode(9)
    root.left.left, root.left.right = TreeNode(7), TreeNode(0)
    root.right.left = TreeNode(0)
    root.right.left.left = TreeNode(0)

    msg = "The problem can be found in the following link:\n"
    msg += "\t'https://leetcode.com/problems/sum-root-to-leaf-numbers/'\n"
    msg += "\tA sample test case is defined in the main function of this file"
    print(msg)
    
    # Actually implement the solution for the test case generated
    slnObj = Solution()
    ans = slnObj.sumNumbers(root)
    # Report ans
    print(f"ans: {ans}")
    return 0

__main__()




        
