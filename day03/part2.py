from collections import defaultdict, namedtuple

with open("input.txt", "r") as f:
    data = f.read().splitlines()


Point = namedtuple("Point", ["x", "y"])

num_tracker: defaultdict[Point, int] = defaultdict(int)

sym_tracker: list[tuple[Point, str]] = list()


for row_idx, row in enumerate(data):
    tmp = ""
    for col_idx, item in enumerate(row):
        if item.isdigit():
            tmp += item
        if not item.isdigit():
            if item != ".":
                sym_tracker.append((Point(col_idx, row_idx), item))

            if tmp:
                for i in range(0, len(tmp)):
                    num_tracker[Point(col_idx - 1 - i, row_idx)] = int(tmp)
                tmp = ""

    if tmp:
        for i in range(0, len(tmp)):
            num_tracker[Point(len(row) - 1 - i, row_idx)] = int(tmp)


total = 0
memo: set[Point] = set()

for pt, sym in sym_tracker:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

    mul_nums = []

    for dx, dy in directions:
        curr = Point(pt.x + dx, pt.y + dy)
        if not (0 <= curr.x < len(data[0])) or not (0 <= curr.y < len(data)):
            continue

        if curr in memo:
            continue

        if not num_tracker[curr]:
            continue

        memo.add(curr)

        tmp = Point(curr.x + 1, curr.y)

        while num_tracker[tmp] and tmp not in memo:
            memo.add(tmp)
            tmp = Point(tmp.x + 1, tmp.y)

        tmp = Point(curr.x - 1, curr.y)

        while num_tracker[tmp] and tmp not in memo:
            memo.add(tmp)
            tmp = Point(tmp.x - 1, tmp.y)

        print(curr, num_tracker[curr])

        if sym == "*":
            print("skipped")
            mul_nums.append(num_tracker[curr])
        # else:
        # total += num_tracker[curr]

    if len(mul_nums) == 2:
        total += mul_nums[0] * mul_nums[1]
        print("2 nums")
        print(mul_nums[0] * mul_nums[1])
    elif len(mul_nums) == 1:
        # total += mul_nums[0]
        print("1 num")
        print(mul_nums[0])


print(total)
