# File: rules/checker_jump.py
class CheckerJump:
    def should_kill(self, board, piece, row, col):
        # Basic jump logic: if the move jumps over an enemy piece
        dr = row - piece.row
        dc = col - piece.col

        if abs(dr) == 2 and abs(dc) == 2:
            middle_row = piece.row + dr // 2
            middle_col = piece.col + dc // 2
            middle_piece = board.get_piece(middle_row, middle_col)
            if middle_piece and middle_piece.player != piece.player:
                return [middle_piece]
        return []
