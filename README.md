# checkers-sim

git add:
✅ Piece capture logic
- rules: for now, pieces can jump over enemy pieces, and capture the piece
- templates: saved sets of game rules

up next:
- [ ] game setup system: instead of hardcoding, make it so that they "pull the game setup from one file or folder". This includes:
  - Defining the board size (8x8 or 11x11) = from checkers to Hnefatafl
  - Placement of pieces when starting the game (this will be part of the saved templates) = so, not checkers anymore more Hnefatafl instead
  - Add another "capture logic" for Hnefatafl (pincers); movement logic is ignored coz we want it to simulate hand picking