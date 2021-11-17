class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                self.dfs(board, i, j)
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                self.dfs(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        return board
    def bfs(self,board, i, j):
        if 0<=i <len(board) and 0<=j<len(board[0]) and board[i][j] == 'O':
            board = '.'
            self.dfs(board, i+1, j)
            self.dfs(board, i-1, j)
            self.dfs(board, i, j+1)
            self.dfs(board, i, j-1)

if __name__ == '__main__':

    x = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    print(Solution().solve(x))