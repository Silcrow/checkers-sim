# File: templates/checkers.py
from rules.checker_jump import CheckerJump

TEMPLATE = {
    "name": "Checkers",
    "kill_rule": CheckerJump(),
    "score_rule": lambda killed: len(killed),
    "win_rule": lambda board, pieces_left: pieces_left[1] == 0 or pieces_left[2] == 0,
}
