class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])

        #find which row it is in
        #cols are sorted so BS
        #then in a row find where again using BS

        if target <matrix[0][0] or target > matrix[ROWS-1][COLS-1]:
            return False

        l,r=0,ROWS-1
        

        while l<r:
            mid=l+(r-l)//2

            if matrix[mid][0]>target:
                #row r has all grater than target
                r=mid-1
            
            if matrix[mid][COLS-1]<target:
                l=mid+1

            if matrix[mid][0]<=target and matrix[mid][COLS-1]>=target:
                l=r=mid
            
        

        mat=matrix[l]

        l,r=0,COLS-1

        while l<=r:
            mid=l+(r-l)//2

            if mat[mid]==target:
                return True
            
            if mat[mid]<target:
                l=mid+1
            if mat[mid]>target:
                r=mid-1
        return False








        