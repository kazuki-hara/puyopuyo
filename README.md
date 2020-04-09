# hara_game

## About
- made a game like PuyoPuyo with Python
- You can check top-10 scores at https://puyopuyo-server.herokuapp.com

## Framework
- client
  - Pygame
  - PySimpleGUI

- server
  - Django

## Features
- You can play a game like PuyoPuyo.
- If four or more Puyo of the same color stick together, they disappear and you can get a score. You can get bonus points by erasing multiple blocks at the same time.
- Each time the block falls 10 times, a disturbing blocks occurs (1 row for less than 3000 points, 2 rows for more).
- After the game is over, your name and score will be sent to the server.

## How to play
1. Enter your name in the popup window.
2. Press space to start the game.
3. Control Puyo (a: roted left, d: roted right, left arrow: move left one row, right arrow: move right one row).
4. Puyo fall fast while holding down space.