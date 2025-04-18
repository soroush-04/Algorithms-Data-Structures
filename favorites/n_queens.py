# n-queen problem
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def backtrack(
            row: int,
            queens: List[int],
            diagonal_main: set,
            diagonal_anti: set,
            queens_column: set,
        ):
            # base case start
            if row == n:
                board = []
                for q in queens:
                    board_row = "." * q + "Q" + (n - q - 1) * "."
                    board.append(board_row)
                result.append(board)
                return

            for col in range(n):
                if is_safe(row, col, diagonal_main, diagonal_anti, queens_column):
                    queens.append(col)
                    queens_column.add(col)
                    diagonal_main.add(row - col)
                    diagonal_anti.add(row + col)

                    backtrack(
                        row + 1, queens, diagonal_main, diagonal_anti, queens_column
                    )

                    queens.pop()
                    queens_column.remove(col)
                    diagonal_main.remove(row - col)
                    diagonal_anti.remove(row + col)

        def is_safe(row, col, diagonal_main, diagonal_anti, queens_column):
            if col in queens_column:
                return False
            if (row - col) in diagonal_main:
                return False
            if (row + col) in diagonal_anti:
                return False
            return True

        # NEVER FORGET TO CALL THE BACKTRACK FUNCTION!!
        backtrack(0, [], set(), set(), set())
        return result
