from functools import reduce

with open("sample.txt", "r") as f:
    data = f.read().split("\n\n")

seeds = list(map(int, data[0].split()[1:]))
mappings = [mapping.strip().split("\n")[1:] for mapping in data[1:]]


def reduce_to_soil(cur, mappings):
    for mapping in mappings:
        dest, src, ran = list(map(int, mapping.split()))

        if cur in range(src, src + ran):
            return cur - src + dest

    return cur


print(min([reduce(reduce_to_soil, mappings, seed) for seed in seeds]))
