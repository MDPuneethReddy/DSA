class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])

        def recur(board, word, r, c, i, j, visited, index):
            if index == len(word):
                return True
            if i < 0 or i >= r or j < 0 or j >= c:
                return False
            if (i, j) in visited:
                return False
            if board[i][j] != word[index]:
                return False

            visited.add((i, j))
            index += 1

            # Explore all four directions
            if (recur(board, word, r, c, i - 1, j, visited, index) or
                recur(board, word, r, c, i + 1, j, visited, index) or
                recur(board, word, r, c, i, j - 1, visited, index) or
                recur(board, word, r, c, i, j + 1, visited, index)):
                return True

            visited.remove((i, j))
            return False

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if recur(board, word, r, c, i, j, set(), 0):
                        return True
        return False

        