class Solution:
    def findWords(self, board, words):
        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                for w in words:
                    if self.dfs(w, i, j, board):
                        ans.append(w)
        return list(set(ans))

    def dfs(self, w, i, j, board):
        if w == '':
            return True

        if len(board) <= i or i < 0 or len(board[0]) <= j or j < 0 or w[0] != board[i][j]:
            return False

        tmp = board[i][j]
        board[i][j] = '#'

        ans = self.dfs(w[1:], i + 1, j, board) or self.dfs(w[1:], i - 1, j, board) or \
              self.dfs(w[1:], i, j - 1, board) or self.dfs(w[1:], i, j + 1, board)

        board[i][j] = tmp

        return ans
if __name__ == '__main__':
    board = [["a","a"]]
    words = ["aa"]
    print(Solution().findWords(board,words))