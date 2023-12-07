from functools import reduce

with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

seeds = list(map(int, data[0].split()[1:]))
mappings = [mapping.strip().split("\n")[1:] for mapping in data[1:]]


def reduce_to_soil(cur, mappings):
    for mapping in mappings:
        dest, src, ran = list(map(int, mapping.split()))

        if cur in range(src, src + ran):
            return cur - src + dest

    return cur


print("part1: ", min([reduce(reduce_to_soil, mappings, seed) for seed in seeds]))

cur_ranges = list(zip(seeds[0::2], seeds[1::2]))

for mapping in mappings:
    new_ranges = []

    while cur_ranges:
        start, length = cur_ranges.pop()
        for m in mapping:
            dst, src, len = map(int, m.split())

            overlap_start = max(start, src)
            overlap_end = min(start + length, src + len)

            if overlap_start < overlap_end:
                new_ranges.append(
                    (overlap_start - src + dst, overlap_end - overlap_start)
                )

                if start < overlap_start:
                    cur_ranges.append((start, overlap_start - start))

                if start + length > overlap_end:
                    cur_ranges.append((overlap_end, start + length - overlap_end))
                break  # breaking will prevent else from getting executed
        else:  # this will run when the loop is not broken
            new_ranges.append((start, length))

    cur_ranges = new_ranges

print("part2: ", min([start for start, _ in cur_ranges]))
