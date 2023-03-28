##############################################################
# LeetCode Template
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
"""

##############################################################
# Link to problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

##############################################################
# My LeetCode solution:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle: return i
        return -1

##############################################################
# Extra code needed to make the LeetCode Solution run
def __main__():
    # First, create the test cases.
    #   NOTE that LeetCode generated most or all of the test cases for me
    msg = "Given two strings needle and haystack, "
    msg += "return the index of the first occurrence "
    msg += "of needle in haystack, or -1 if needle "
    msg += "is not part of haystack."
    print(msg)
    print("Input the strings below:")
    haystack = input("  haystack: ")
    needle   = input("    needle: ")
    
    # Actually implement the solution for the test case generated
    slnObj = Solution()
    ans = slnObj.strStr(haystack, needle)
    # Report ans
    if ans == -1: print(f"\"{needle}\" does NOT occur in \"{haystack}\"")
    else: print(f"\"{needle}\" occur in \"{haystack}\" at index {ans}")
    return 0

__main__()