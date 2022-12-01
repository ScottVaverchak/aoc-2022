#!/usr/bin/env python3

with open("input.txt") as f:
    content = list(map(sum, [[int(y) for y in x.split('\n')] for x in f.read().split('\n\n')]))
    content.sort(reverse=True)
    print(f"Answer: {content[0]}")

