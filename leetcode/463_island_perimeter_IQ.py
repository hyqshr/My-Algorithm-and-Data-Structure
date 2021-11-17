class Solution:
    def islandPerimeter(self, grid) -> int:
        l1,l2 = len(grid),len(grid[0])
        ans = 0
        for i in range(l1):
            for j in range(l2):
                adj = 0
                if grid[i][j] == 1:
                    for x,y in [(i-1,j),(i+1,j),(i,j+1),(i,j-1)]:
                        if l1> x >= 0 and l2> y >= 0 and grid[x][y] == 1:
                            adj += 1
                    ans += 4 - adj
        return ans
if __name__ == '__main__':
    x = grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(Solution().islandPerimeter(x))