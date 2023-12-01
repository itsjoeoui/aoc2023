total = 0

with open("input.txt") as f:
    for line in f:
        num = ""
        line = line.strip()

        tmp = ""
        for char in line:
            if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if tmp == "":
                    num = char
                tmp = char
        num += tmp
        total += int(num)

print(total)
