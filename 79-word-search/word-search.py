class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recurr(board,word,visited,wordind,i,j,height,width):
            if wordind==len(word):
                return True
            if i==height or i<0 or j==width or j<0:
                return False
            if [i,j] in visited:
                return False
            if board[i][j]!=word[wordind]:
                return False
            visited.append([i,j])
            value=recurr(board,word,visited,wordind+1,i+1,j,height,width) or recurr(board,word,visited,wordind+1,i-1,j,height,width) or recurr(board,word,visited,wordind+1,i,j+1,height,width) or recurr(board,word,visited,wordind+1,i,j-1,height,width)
            visited.pop()
            return value
            
            
        height=len(board)
        width=len(board[0])
        value=False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    value=value or recurr(board,word,[],0,i,j,height,width)
        return value

        