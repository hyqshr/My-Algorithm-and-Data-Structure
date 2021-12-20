class Solution:
    def numIslands(self) -> int:
        mode = False
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if gird[i][j] == "1" and mode == False:
                    mode = True
                    res += 1
                elif gird[i][j] == '1' and mode == True:
                    if (len(grid) > i - 1 >= 0 and gird[i - 1][j] == '1') or (
                            len(grid[0]) > j - 1 >= 0 and gird[i][j - 1] == '1'):
                        continue
                    elif (len(grid) > i - 1 >= 0 and gird[i - 1][j] == '0') and (
                            len(grid[0]) > j - 1 >= 0 and gird[i][j - 1] == '0'):
                        res += 1
                    else:
                        continue
        return res
