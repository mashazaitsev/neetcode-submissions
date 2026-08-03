class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidBlock(board) and self.isValidRow(board) and self.isValidColumn(board)
    
    def isValidBlock(self, board: List[List[str]]):
        rows,cols=len(board),len(board[0])
        blocks=rows
        blockSize=int(rows**0.5)
        for blockNum in range(blocks):
            startRow=blockNum//blockSize*blockSize
            startCol=(blockNum%blockSize)*blockSize
            endRow=startRow+3 #inclusive for range
            endCol=startCol+3
            numsInRow=[] #resets every block
            for row in range(startRow,endRow):
                for col in range(startCol,endCol):
                    if board[row][col].isdigit():
                        numsInRow.append(int(board[row][col]))
            if len(set(numsInRow))<len(numsInRow):
                return False
        return True 

    def isValidRow(self, board: List[List[str]]):
        rows,cols=len(board),len(board[0])
        for row in range (rows):
            numsInRow=[] #resets every row
            for col in range(cols):
                if board[row][col].isdigit(): #track if int
                    numsInRow.append(int(board[row][col]))  
            if len(set(numsInRow))<len(numsInRow):
                return False
        return True

    def isValidColumn(self, board: List[List[str]]):
        rows,cols=len(board),len(board[0])
        for col in range(cols):
            numsInCol=[] #resets every col
            for row in range(rows):
                if board[row][col].isdigit():
                    numsInCol.append(int(board[row][col]))
            if len(set(numsInCol))<len(numsInCol):
                return False
        return True #once you check all cases

                

        