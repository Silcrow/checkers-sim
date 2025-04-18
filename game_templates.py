# File: game_templates.py
def load_template(name):
    if name == "hnefatafl":
        # 11x11 board with attacker/defender positions
        setup = [
            # Defenders
            (5, 5, "king", 1),
            (4, 5, "pawn", 1), (6, 5, "pawn", 1),
            (5, 4, "pawn", 1), (5, 6, "pawn", 1),
            # Attackers
            (0, 5, "pawn", 2), (10, 5, "pawn", 2),
            (5, 0, "pawn", 2), (5, 10, "pawn", 2),
            (3, 5, "pawn", 2), (7, 5, "pawn", 2),
            (5, 3, "pawn", 2), (5, 7, "pawn", 2)
        ]
        return {"rows": 11, "cols": 11, "setup": setup}
    else:
        raise ValueError("Unknown template name: " + name)
