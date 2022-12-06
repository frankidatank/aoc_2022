N = 9
drawing_lines = 8


def q1():
    with open("./input.txt") as fin:
        parts = fin.read()[:-1].split("\n\n")
        drawing = parts[0].split("\n")
        stacks = [[] for _ in range(N)]

        for i in range(drawing_lines):
            line = drawing[i]
            crates = line[1::4]
            for s in range(len(crates)):
                if crates[s] != " ":
                    stacks[s].append(crates[s])

    # Reverse all stacks
    stacks = [stack[::-1] for stack in stacks]

    # Move things around
    for line in parts[1].split("\n"):
        tokens = line.split(" ")
        n, src, dst = map(int, [tokens[1], tokens[3], tokens[5]])
        src -= 1
        dst -= 1
        pops = []
        for _ in range(n):
            if stacks[src]:
                pops.append(stacks[src].pop())
        stacks[dst].append(pops[::-1])

    tops = [stack[-1] for stack in stacks]
    print("".join(tops))


def q2():
    with open("./input.txt") as fin:
        parts = fin.read()[:-1].split("\n\n")
        drawing = parts[0].split("\n")
        stacks = [[] for _ in range(N)]

        for i in range(drawing_lines):
            line = drawing[i]
            crates = line[1::4]
            for s in range(len(crates)):
                if crates[s] != " ":
                    stacks[s].append(crates[s])

    # Reverse all stacks
    stacks = [stack[::-1] for stack in stacks]

    # Move things around
    for line in parts[1].split("\n"):
        tokens = line.split(" ")
        n, src, dst = map(int, [tokens[1], tokens[3], tokens[5]])
        src -= 1
        dst -= 1

        stacks[dst].extend(stacks[src][-n:])
        stacks[src] = stacks[src][:-n]

    tops = [stack[-1] for stack in stacks]
    print("".join(tops))


def main():
    # q1()
    q2()


if __name__ == "__main__":
    main()
