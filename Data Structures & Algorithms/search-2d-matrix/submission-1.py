class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Find the row that contains the range of target
        l = 0; r = len(matrix)-1
        prev = -1
        row = 0
        while l <= r:
            mid = l+(r-l)//2
            if matrix[mid][0] > target:
                r = mid-1
            else:
                if len(matrix)-2 <mid or matrix[mid+1][0] > target:
                    row = mid
                    break
                else:
                    l = mid+1
        l = 0; r = len(matrix[row])-1

        while l<=r:
            mid = l + (r-l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False






        return True



        
        
        
        #Then do a binary search in the row
