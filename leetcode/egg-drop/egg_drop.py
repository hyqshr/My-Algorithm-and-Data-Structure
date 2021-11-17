class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[float('inf')] * (N + 1) for _ in range(K + 1)]
        #类似fibonacci 的0,1是basecase,0台阶那就是0，1个就是1
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1

        #只剩一个蛋，那么n是多少，你就得试几次
        for j in range(1, N + 1):
            dp[1][j] = j

        for i in range(2, K + 1):
            for j in range(2, N + 1):
                for k in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]))
                    print('i: {},j: {}'.format(i,j))
                    print('dp[{}][{}],  dp[{}][{}]'.format(i-1,k-1,i,j-k))
        return dp[K][N]

if __name__ == '__main__':
    print(Solution().superEggDrop(2,10))