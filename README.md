# checkers-sim

git add:
- [ ] look at how it works (what changed in the files)
Hnefatafl is achieved (only scoring left)
- Defining the board size (8x8 or 11x11) = from checkers to Hnefatafl
- Placement of pieces when starting the game (this will be part of the saved templates) = so, not checkers anymore more Hnefatafl instead
- Add another "capture logic" for Hnefatafl (pincers); movement logic is ignored coz we want it to simulate hand picking

up next:
- fix the pieces starting positions for Hnefatafl
- add rules: move like a chess king, capture via "flanking" (similar to pincers but any 2 enemy units adjacent with 2 tiles apart counts),
engagement logic (when an enemy is adjacent, it cannot disengage), disengagement logic (when 2+ is engaging, one of them can disengage, as long as 1 is always engaging it),
- scoring rules work just like capture rules. It's another folder. Make 3 scoring and winning conditions:
  - counting enemy captures and winning when reaching a number.
  - winning by placing the king on the corner tiles
  - winning by capturing the king
- You only need a winning logic for either player. When one wins, the other instantly loses.

- capture by placing a piece on the enemy (like chess)
- thrusting logic = no game logic, just player aware to eat a piece by placing it on the enemy then putting it back.

last stages: make NPC and surrogate
- make PvE NPC = movement restriction logic will be inside the NPC. Instead of the board controlling how pieces move. Do it as if
NPCs vow to play the game with honor and recognize how to not move a piece. That would be more realistic and flexible.
You're not simulating pieces that restrict what can happen. You're simulating NPCs intentionally playing by the rules with
a virtual table-top props.
- make a surrogate = copy the NPC, but to represent you, to automate you playing.
- make an analyst = as if 2 ppl are playing an a third person is watching, taking notes and concluding insights.
- maybe these 3 systems will be a separate repo? I'm not sure how they would see and touch this board.
I'm thinking maybe bash of some sort, coz making them interpret visuals is overkill.

optional:
- fixed obstacles = tiles no piece can move through (so you can make fox and geese, and also trees/rocks on the map)
- movement rule = can move x number of tiles
- shooting rule = can capture units within range (I want this modular, so some can capture with knight range, some with bishop)
movement and shooting completes what I see in modern tabletop games.