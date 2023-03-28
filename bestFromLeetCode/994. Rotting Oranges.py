##############################################################
# LeetCode Template
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
"""

##############################################################
# Link to problem: https://leetcode.com/problems/rotting-oranges/

##############################################################
# My LeetCode solution:
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # stack gets automatically updated each time
        def solveNext(stack, state) -> set:
            # stack contains the rows and cols of fresh oranges about to go rotten
            # state is the current state of the board
            todo = set() # Add new elements to this temporary stack
            while stack:
                row, col = stack.pop()
                if row > 0 and state[row-1][col] == 1:
                    todo.add((row-1, col))
                    state[row-1][col] = 2
                if row < len(state) - 1 and state[row+1][col] == 1:
                    todo.add((row+1, col))
                    state[row+1][col] = 2
                if col > 0 and state[row][col-1] == 1:
                    todo.add((row, col-1))
                    state[row][col-1] = 2
                if col < len(state[row]) - 1 and state[row][col+1] == 1:
                    todo.add((row, col+1))
                    state[row][col+1] = 2
            return todo
        
        # Initializations
        #state = [[grid[row][col] for col in range(len(grid[row]))] for row in range(len(grid))]
        state = grid
        # Create the initial stack
        stack = set()
        for row, _ in enumerate(grid):
            for col, _ in enumerate(grid[row]):
                if grid[row][col] == 2:
                    stack.add((row, col))
        ans = -1 if stack else 0
        while stack:
            #print(stack)
            #print(state)
            ans += 1
            stack = solveNext(stack, state)
        #print(state)
        # If there exists a fresh orange in state, return -1
        for row, _ in enumerate(state):
            for _, val in enumerate(state[row]):
                if val == 1:
                    return -1
        return ans

##############################################################
# Extra code needed to make the LeetCode Solution run
def __main__():
    # First, create the test cases.
    #   NOTE that LeetCode generated most or all of the test cases for me
    grid = [[0,0,0],
            [1,2,0],
            [0,2,2],
            [1,0,1]]
    
    # Actually implement the solution for the test case generated
    slnObj = Solution()
    ans = slnObj.orangesRotting(grid)
    # Report ans
    print(ans)
    return 0

__main__()