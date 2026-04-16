class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # don't need to solve the sudoku, just simply verify the board
        # given is not invalid

        # 3 primary helper functions to ensure the rules aren't violated
        # if any of the 3 are violated then the value is false


        # isValidRow(list)
        # isValidColumn(list)
        # isValidBox(list,list)

        # WRONG - just make 3 hash sets... if the value we are reading is already in during insertion then its a fail
        # if its a "." then continue
        # if its not in the hash set then add it and continue

        # by just doing a simple iteration on each box, we can verify that boxes validity in each of the 3 rules:
            # if its good in the row
            # if its good in the column
            # if its good in the 3x3 box
        # on each pop of the row / column / box we need to clear the relevant set to reset it

        # really need a dict of sets, so we can match each row (or column) to a set and if we are back on that 
            # row or column we can check that specific set it maps to see if we fail the check or not

        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val == ".":
                    continue

                # current val exists in the row
                already_exists_in_row = val in rows[r]
                already_exists_in_col = val in columns[c]
                already_exists_in_square = val in squares[(r // 3 ,c // 3)]

                if already_exists_in_row or already_exists_in_col or already_exists_in_square:
                    return False
                
                # otherwise its valid and append to each of those
                rows[r].add(val)
                columns[c].add(val)
                squares[(r // 3 ,c // 3)].add(val)
        return True

                
