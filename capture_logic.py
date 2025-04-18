# File: capture_logic.py
class PincerCapture:
    def apply(self, board, moved_piece):
        row, col = moved_piece.row, moved_piece.col
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            opp_row = row + dr
            opp_col = col + dc
            cap_row = row + 2 * dr
            cap_col = col + 2 * dc

            if 0 <= opp_row < board.rows and 0 <= opp_col < board.cols and \
               0 <= cap_row < board.rows and 0 <= cap_col < board.cols:

                mid_piece = board.get_piece(opp_row, opp_col)
                end_piece = board.get_piece(cap_row, cap_col)

                if mid_piece and mid_piece.player != moved_piece.player:
                    if end_piece and end_piece.player == moved_piece.player:
                        board.board[opp_row][opp_col] = None  # captured
