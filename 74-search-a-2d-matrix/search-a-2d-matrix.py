class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarysearch():
            top=0
            bottom=len(matrix)
            while(top<bottom):
                mid=bottom+((top-bottom)//2)
                print("mid",mid)
                if target>=matrix[mid][0] and target<=matrix[mid][len(matrix[0])-1]:
                    return mid
                elif target<matrix[mid][0]:
                    bottom=mid-1
                else:
                    top=mid+1
            return top
            
        value=binarysearch()
        if value>=len(matrix):
            return False
        print("value",value)
        left=0
        right=len(matrix[0])-1
        while(left<=right):
            mid=left+((right-left)//2)
            print("mid",mid)
            if matrix[value][mid]==target:
                return True
            elif matrix[value][mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
        
        
        