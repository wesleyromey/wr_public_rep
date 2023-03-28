##############################################################
# LeetCode Template
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
"""

##############################################################
# Link to problem: https://leetcode.com/problems/flood-fill/

##############################################################
# My LeetCode solution:
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        stack = [(sr,sc)]
        #alreadyVisited = dict() # alreadyVisited = {row1: {col1, col2, ...}, row2: {...}, ...}
        origColor = image[sr][sc]
        if color == origColor:
            return image
        while stack:
            row, col = stack.pop()
            image[row][col] = color
            if row < len(image) - 1 and image[row+1][col] == origColor:
                image[row+1][col] = color
                stack.append((row + 1, col))
            if col < len(image[row]) - 1 and image[row][col+1] == origColor:
                image[row][col+1] = color
                stack.append((row, col + 1))
            if row > 0 and image[row-1][col] == origColor:
                image[row-1][col] = color
                stack.append((row - 1, col))
            if col > 0 and image[row][col-1] == origColor:
                image[row][col-1] = color
                stack.append((row, col - 1))
        return image

##############################################################
# Extra code needed to make the LeetCode Solution run
def __main__():
    # First, create the test cases.
    #   NOTE that LeetCode generated most or all of the test cases for me
    image = [[1,2,2,3],[2,2,2,2],[3,2,3,3]]
    sr, sc, color = 1, 1, 5
    
    # Actually implement the solution for the test case generated
    slnObj = Solution()
    ans = slnObj.floodFill(image, sr, sc, color)
    # Report ans
    print(ans)
    return 0

__main__()