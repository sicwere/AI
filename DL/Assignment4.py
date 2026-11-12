from itertools import chain

class SudokuSquare:
    def __init__(self,sg,row,col,val=0):
        self.subgrid = sg
        self.row = row
        self.col = col
        self.val = val

    def print(self):
        print (self.subgrid,self.row,self.col,self.val)

class SudokuSubgrid:
    DIGITS = {n for n in range(1,10)}

    def __init__(self,id,square_list):
        self.id = id
        self.squares = []
        for i in range(9):
            self.squares.append(SudokuSquare(id,i//3,i%3,square_list[i]))
        
    def get_row_vals(self,r):
        return [s.val for s in self.squares if s.row == r and s.val != 0]
    
    def get_col_vals(self,c):
        return [s.val for s in self.squares if s.col == c and s.val != 0]
    
    def get_empty_cells(self):
        return [s for s in self.squares if s.val == 0]
    
    def get_unused_vals(self):
        return list(SudokuSubgrid.DIGITS & set([v for v in self.squares.val if v != 0]))

    def print(self):
        for s in self.squares:
            s.print()

class SudokuGrid:
    def __init__(self,square_lists):
        self.subgrids = []
        for i in range(9):
             self.subgrids.append(SudokuSubgrid(i,square_lists[i]))

    def get_empty_cells(self):
        return list(chain.from_iterable(sq.get_empty_cells() for sq in self.subgrids))

    def print(self):
        for sg in self.subgrids:
            sg.print()

sudoku_board = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],
    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],
    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0]
]  

sudoku_grid = SudokuGrid(sudoku_board)
print(len(sudoku_grid.get_empty_cells()))