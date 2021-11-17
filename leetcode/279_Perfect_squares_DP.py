class Solution:
    def numSquares(self,n):
        dp = [0] + [float('inf')]*n
        for i in range(1, n+1):

            x = []
            print('dp: ',dp)
            print('i is ',i,'  The range of j is: ',range(1, int(i**0.5)+1))

            ###only this line is useful
            ###only this line is useful
            ###only this line is useful
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
            ###only this line is useful
            ###only this line is useful
            ###only this line is useful

            for j in range(1, int(i ** 0.5) + 1):
                x.append(dp[i-j*j])
                print('append dp[i-j*j] : dp[{} - {}] to x, which is'.format(i,j*j), dp[i-j*j])
            print('we take the minimum from x and then plus 1, x is :',x,'so dp[{}] = '.format(i),min(x)+1)
            print('\n')
        return dp[n]

if __name__ == '__main__':
    n = 13
    Solution().numSquares(n)
