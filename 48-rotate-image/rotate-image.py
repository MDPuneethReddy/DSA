class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)-1):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for i in matrix:
            for j in range(len(i)//2):
                i[j],i[len(i)-j-1]=i[len(i)-j-1],i[j]
        

        

        