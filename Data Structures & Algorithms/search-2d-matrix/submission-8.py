class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])

        #find row
        top=0
        bot=ROWS-1
        row=0

        while top<=bot:
            
            row=top+(bot-top)//2

            if target<matrix[row][0]:
                bot=row-1
             
            elif target>matrix[row][COLS-1]:
                top=row+1
                
            else:
                break
   
        
        #found row
        l,r=0,COLS-1
        while l<=r:
            m=l+(r-l)//2
            print(matrix[row][m])
            if target==matrix[row][m]:
                return True
            if target < matrix[row][m]:
                r=m-1
            else:
                l=m+1
        
        return False
        



        