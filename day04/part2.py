import re
from collections import defaultdict

with open("input.txt", "r") as f:
    data = f.read().splitlines()

total = 0

tracking: defaultdict[int, int] = defaultdict(lambda: 1)

for line in data:
    game_meta, info = line.split(":")
    _, game_num = re.split(r"\s+", game_meta)

    game_num = int(game_num)

    num_copies = tracking[int(game_num)]

    guess, win = info.split("|")

    guess = guess.strip().split()
    win = win.strip().split()

    winning_count = 0
    for item in guess:
        if item in win:
            winning_count += 1

    for _ in range(winning_count):
        game_num += 1
        tracking[game_num] += num_copies

    total += winning_count * num_copies

print(total + len(data))
