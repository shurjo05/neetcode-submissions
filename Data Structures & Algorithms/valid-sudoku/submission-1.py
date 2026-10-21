class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenCols = [set() for _ in range(len(board))]
        seenSq = [set() for _ in range(len(board))]
        for i, rows in enumerate(board):
            seenRow = set()
            for j, n in enumerate(rows):
                if n == ".":
                    continue
                if n in seenRow:
                    return False
                if n in seenCols[j]:
                    return False
                if n in seenSq[i//3 * 3 + j//3]:
                    return False
                seenSq[i//3 * 3 + j//3].add(n)
                seenCols[j].add(n)
                seenRow.add(n)
        return True