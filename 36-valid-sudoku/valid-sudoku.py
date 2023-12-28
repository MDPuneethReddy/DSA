class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows(board):
            for i in board:
                s=set()
                for j in i:
                    if j!="." and j in s:
                        return False
                    else:
                        s.add(j)
            return True
        def checkColumns(board):
            for i in range(len(board)):
                s=set()
                j=0
                while(j<len(board)):
                    if board[j][i]!="." and board[j][i] in s:
                        return False
                    else:
                        s.add(board[j][i])
                    j+=1
            return True  

        def checkGrid(board):
            i=0
            j=0
            while(i<len(board)):
                # print(i,j)
                values=[board[i][j],board[i+1][j],board[i+2][j],board[i][j+1],board[i][j+2],board[i+1][j+1],board[i+1][j+2],board[i+2][j+1],board[i+2][j+2]]
                mainValues=set()
                for value in values:
                    if value!="." and value in mainValues:
                        return False
                    else:
                        mainValues.add(value)
                j+=3  
                if j>=len(board):
                    i+=3   
                    j=0
            return True             

        return checkRows(board) and checkColumns(board) and checkGrid(board)
        