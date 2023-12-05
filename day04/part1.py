with open("input.txt", "r") as f:
    data = f.read().splitlines()

total = 0

for line in data:
    times = 0
    _, info = line.split(":")
    guess, win = info.split("|")

    guess = guess.strip().split()
    win = win.strip().split()

    for item in guess:
        if item in win:
            times += 1

    if times > 0:
        total += 2 ** (times - 1)

print(total)
