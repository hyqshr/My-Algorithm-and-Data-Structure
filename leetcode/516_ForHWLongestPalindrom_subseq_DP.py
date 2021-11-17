from leetcode.utils import printList
# Function to find LCS of `X[0…m-1]` and `Y[0…n-1]`
def findLongestPalindrome(X, Y, m, n, lookup):

    if m == 0 or n == 0:
        return ""

    # If the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
        # append current character (`X[m-1]` or `Y[n-1]`) to LCS of
        # substring `X[0…m-2]` and `Y[0…n-2]`
        return findLongestPalindrome(X, Y, m - 1, n - 1, lookup) + X[m - 1]

    # otherwise, if the last character of `X` and `Y` are different

    # if a top cell of the current cell has more value than the left
    # cell, then drop the current character of string `X` and find LCS
    # of substring `X[0…m-2]`, `Y[0…n-1]`

    if lookup[m - 1][n] > lookup[m][n - 1]:
        return findLongestPalindrome(X, Y, m - 1, n, lookup)

    # if a left cell of the current cell has more value than the top
    # cell, then drop the current character of string `Y` and find LCS
    # of substring `X[0…m-1]`, `Y[0…n-2]`

    return findLongestPalindrome(X, Y, m, n - 1, lookup)


# Function to find the length of LCS of substring `X[0…n-1]` and `Y[0…n-1]`
def LCSLength(X, Y, n, lookup):
    # Fill the lookup table in a bottom-up manner.
    # The first row and first column of the lookup table are already 0.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # if current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1

            # otherwise, if the current character of `X` and `Y` don't match
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])

    return lookup[n][n]


if __name__ == '__main__':
    X = 'bbbab'

    # string `Y` is a reverse of `X`
    Y = X[::-1]

    # lookup[i][j] stores the length of LCS of substring `X[0…i-1]` and `Y[0…j-1]`
    lookup = [[0 for x in range(len(X) + 1)] for y in range(len(X) + 1)]
    # find the length of the LPS using LCS
    print('The length of the longest palindromic subsequence is',
          LCSLength(X, Y, len(X), lookup))
    printList(lookup)

    # print the LPS using a lookup table
    print('The longest palindromic subsequence is',
          findLongestPalindrome(X, Y, len(X), len(X), lookup))