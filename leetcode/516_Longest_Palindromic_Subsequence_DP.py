from leetcode.utils import printList
class Solution:
    #bottom-up
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        p = []
        for i in range(n - 1, -1, -1):
            print('i = ',i)
            dp[i][i] = 1

            for j in range(i+1, n):
                print('\tj = ', j)

                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    print('s[i] == s[j]','dp[i][j] = dp[i + 1][j - 1] + 2 = ',dp[i + 1][j - 1],'+ 2 = ',dp[i][j])
                    p.append(s[j])

                else:
                    print('s[i]: {},s[j]: {}不相等,max(dp[i + 1][j], dp[i][j - 1]) = max({},{})'.format(s[i],s[j],dp[i + 1][j],dp[i][j - 1]))
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                printList(dp)
        print(p)
        return dp[0][n - 1]
    #top_down
    def findLongestPalindrome(self,X, i, j):

        # Base condition
        if i > j:
            return 0

        # If the string `X` has only one character, it is a palindrome
        if i == j:
            return 1

        # If the last character of the string is the same as the first character
        if X[i] == X[j]:
            # include the first and last characters in palindrome
            # and recur for the remaining substring `X[i+1, j-1]`
            print('相等, func({}, {} + 1, {} - 1 ) + 2'.format(X, i, j ))
            return self.findLongestPalindrome(X, i + 1, j - 1) + 2

        '''
          If the last character of the string is different from the first character
            1. Remove the last character and recur for the remaining substring
               `X[i, j-1]`
            2. Remove the first character and recur for the remaining substring
               `X[i+1, j]`
        '''

        # Return the maximum of the two values
        print('不相等, func({}, {} + 1, {} - 1 ) + 2'.format(X, i + 1, j - 1))

        return max(self.findLongestPalindrome(X, i, j - 1), self.findLongestPalindrome(X, i + 1, j))


if __name__ == '__main__':
    #Solution().longestPalindromeSubseq('bbbab')
    print(Solution().findLongestPalindrome('bbbab',0,4))
