class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])

        l=0
        r=len(matrix)-1
       
        

        while l<r:
            m=l+(r-l)//2

            if target==matrix[m][0]:
                return True

            if target < matrix[m][0]:
                r=m-1
            else:
                l=m+1
        
        #l is the row to check
        row=l
        l=0
        r=(len(matrix[0]))-1

        while l<=r:
            m=l+(r-l)//2

            if target==matrix[row][m]:
                return True
            
            if target<matrix[row][m]:
                r=m-1
            else:
                l=m+1
        
        return False






        