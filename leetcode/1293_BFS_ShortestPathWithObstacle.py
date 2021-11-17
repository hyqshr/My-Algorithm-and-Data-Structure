# from collections import deque
# class Solution:
#     def shortestPath(self, grid, k: int) -> int:
#         if len(grid) == 1 and len(grid[0]) == 1:
#             return 0
#
#         queue = deque([(0,0,k,0)])
#         visited = set([(0,0,k)])
#
#         if k > (len(grid)-1 + len(grid[0])-1):
#             return len(grid)-1 + len(grid[0])-1
#
#         while queue:
#             row, col, eliminate, steps = queue.popleft()
#             for new_row, new_col in [(row-1,col), (row,col+1), (row+1, col), (row, col-1)]:
#                 if (new_row >= 0 and
#                     new_row < len(grid) and
#                     new_col >= 0 and
#                     new_col < len(grid[0])):
#                     #有墙，有技能点(eliminate)，且未访问
#                     if grid[new_row][new_col] == 1 and eliminate > 0 and (new_row, new_col, eliminate-1) not in visited:
#                         visited.add((new_row, new_col, eliminate-1))
#                         queue.append((new_row, new_col, eliminate-1, steps+1))
#                     #如果没有墙，且未访问
#                     if grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
#                         #是否到达终点?
#                         if new_row == len(grid)-1 and new_col == len(grid[0])-1:
#                             return steps+1
#                         #若不是终点，添加当前的位置
#                         visited.add((new_row, new_col, eliminate))
#                         queue.append((new_row, new_col, eliminate, steps+1))
#
#         return -1
from collections import deque


class Solution:
    def shortestPath(self, grid , k: int) -> int:

        queue = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])

        while queue:
            row, col, elim, step = queue.popleft()

            for new_row, new_col in [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]:
                if new_row >= 0 and new_col >= 0 and new_row < len(grid) and new_col < len(grid[0]):

                    if grid[new_row][new_col] == 1 and (new_row, new_col, elim - 1) not in visited:
                        visited.add((new_row, new_col, elim - 1))
                        queue.append((new_row, new_col, elim - 1, step + 1))

                    if grid[new_row][new_col] == 0:
                        if new_row == len(grid) - 1 and new_col == len(grid[0]) - 1:
                            return step + 1
                        visited.add((new_row, new_col, elim))
                        queue.append((new_row, new_col, elim, step + 1))
            return -1
if __name__ == '__main__':
    grid =[[0, 0, 0],
         [1, 1, 0],
         [0, 0, 0],
         [0, 1, 1],
         [0, 0, 0]]
    k = 1
    Solution().shortestPath(grid,k)