class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #definetly uses hashsets. add to a hash and then check if the hash increased in size
        #do for every row, every column, and every block
        

            
        for i in range(9):
            
            colCount = set()
            countCol = 0
            rowCount = set()
            countRow = 0
            #get rows
            for a in range(9):
                if board[i][a] != ".":
                    countRow+=1
                    rowCount.add(board[i][a])
                    print(f"row: {a}")
                    print(rowCount)
                    print(countRow)
            
            if countRow != len(rowCount):
                return False
            for j in range(9):
                if board[j][i] != ".":
                    countCol +=1
                    colCount.add(board[j][i])
            if countCol != len(colCount):
                return False

            #getblocks
        for i in range(3):
            for j in range(3):
                blockCount = set()
                countBlock = 0
                for k in range(3):
                    for n in range(3):
                        if board[i*3+k][j*3+n] != ".":
                            countBlock+=1
                            blockCount.add(board[i*3+k][j*3+n])
                if countBlock != len(blockCount):
                    return False
            
        


        return True