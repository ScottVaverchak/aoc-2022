#!/usr/bin/env python3

from game import Game

with open("input.txt") as f:
    content = [(x[0], x[2]) for x in f.readlines()]
    game = Game(content)
    scores = game.play()

    print(f"Your Score:  {scores[1]}")
    print(f"Elves Score: {scores[0]}")