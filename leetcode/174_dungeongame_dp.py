from leetcode import utils as util


#巧妙：
#min(float('inf'),1)任何数 num 与 inf 取 min 都返回num,用这个控制计算，有真实数字的dungeon
#如果位置为正数，就是会恢复勇士血量的格子，根据max方法会变成1，代表你只要有1HP就能到这个位置。（0就挂了）
class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        #我们需要右下角目标位置的cost 加上 1的血量作为到达这里所需要的血量
        # 因此要把dp对应的right 和down设置为1，否则如果是-2，由于min怎么都只返回inf,14行只会返回1
        dp[m - 1][n], dp[m][n - 1] = 1, 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)

                #以下为辅助打印部分
                print('dp[i + 1][j], dp[i][j + 1]) is {}'.format((dp[i + 1][j], dp[i][j + 1])),' min is ',min(dp[i + 1][j], dp[i][j + 1]))
                print('dungeon is ',dungeon[i][j],'min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j] is ',min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
                print('we got ',dp[i][j])
                util.printList(dp)

        return dp[0][0]

if __name__ == '__main__':
    x = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    Solution().calculateMinimumHP(x)