# File: game_templates.py
def load_template(name):
    if name == "hnefatafl":
        # 11x11 board with attacker/defender positions
        hnefatafl_setup = [
            # King
            (5, 5, "king", 1),

            # Defenders surrounding the king (N, S, E, W)
            (4, 5, "pawn", 1), (6, 5, "pawn", 1),
            (5, 4, "pawn", 1), (5, 6, "pawn", 1),

            # Defenders on diagonals around the king
            (4, 4, "pawn", 1), (4, 6, "pawn", 1),
            (6, 4, "pawn", 1), (6, 6, "pawn", 1),

            # Defenders forming a plus shape from the king
            (3, 5, "pawn", 1), (7, 5, "pawn", 1),
            (5, 3, "pawn", 1), (5, 7, "pawn", 1),

            # Attackers at top, bottom, left, and right edges
            (0, 3, "pawn", 2), (0, 4, "pawn", 2), (0, 5, "pawn", 2), (0, 6, "pawn", 2), (0, 7, "pawn", 2),
            (10, 3, "pawn", 2), (10, 4, "pawn", 2), (10, 5, "pawn", 2), (10, 6, "pawn", 2), (10, 7, "pawn", 2),
            (3, 0, "pawn", 2), (4, 0, "pawn", 2), (5, 0, "pawn", 2), (6, 0, "pawn", 2), (7, 0, "pawn", 2),
            (3, 10, "pawn", 2), (4, 10, "pawn", 2), (5, 10, "pawn", 2), (6, 10, "pawn", 2), (7, 10, "pawn", 2),

            # Attackers near the center (reinforcing the edges)
            (5, 1, "pawn", 2), (5, 9, "pawn", 2),
            (1, 5, "pawn", 2), (9, 5, "pawn", 2)
        ]
        return {"rows": 11, "cols": 11, "setup": hnefatafl_setup}
    else:
        raise ValueError("Unknown template name: " + name)
