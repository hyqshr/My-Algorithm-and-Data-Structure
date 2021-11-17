class Solution:
    def isMatch(self, s, p):
        dp = [[False for _ in range(len(p) + 1)] for i in range(len(s) + 1)]
        dp[0][0] = True

        #如果是连续的*,则给T，只要有一个不是consecutive,break it
        for j in range(1, len(p) + 1):
            if p[j - 1] != '*':
                break
            dp[0][j] = True


        #按照阅读顺序
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] in {s[i - 1], '?'}:
                    dp[i][j] = dp[i - 1][j - 1]

                #如果是 '*',请记住！！！两种情况：空字符与非空字符
                    #d[i-1][j]:  *代表了空字符: ab,ab*
                    #d[i][j-1]:  *代表了非空字符, abc,ab*

                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]

if __name__ == '__main__':
    s = 'adceb'
    p = '*a*b'
    Solution().isMatch(s,p)