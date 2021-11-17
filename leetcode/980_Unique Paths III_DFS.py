from leetcode.utils import printList
class Solution:
    def uniquePathsIII(self, A):
        self.res = 0
        m, n, empty = len(A), len(A[0]), 1
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    x, y = (i, j)
                elif A[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty,d = 1):
            printList(A)
            print(x,y,d)
            if not (0 <= x < m and 0 <= y < n and A[x][y] >= 0): return
            if A[x][y] == 2:
                self.res += empty == 0
                print('添加！')
                return
            A[x][y] = -2
            dfs(x + 1, y, empty - 1,d+1)
            dfs(x - 1, y, empty - 1,d+1)
            dfs(x, y + 1, empty - 1,d+1)
            dfs(x, y - 1, empty - 1,d+1)
            print('触发了')
            A[x][y] = 0

        dfs(x, y, empty)
        return self.res

if __name__ == '__main__':
    grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    Solution().uniquePathsIII(grid)
