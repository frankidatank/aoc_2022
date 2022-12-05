# find occurences where an input fully overlaps another
def q1(lines):
    count = 0
    for input in lines:
        input = input.strip()
        input = input.split("-")
        input[1] = input[1].split(",")
        first = {int(input[0]), int(input[1][0])}
        second = {int(input[1][1]), int(input[2])}
        if first[0] >= second[0] and first[1] <= second[1]:
            count += 1
        elif second[0] >= first[0] and second[1] <= first[1]:
            count += 1

    return count

# find if overlap at all


def q2(lines):
    count = 0
    for input in lines:
        input = input.strip()
        input = input.split("-")
        input[1] = input[1].split(",")
        first = [int(input[0]), int(input[1][0])]
        second = [int(input[1][1]), int(input[2])]
        lap1 = {num for num in range(first[0], first[1] + 1)}
        lap2 = {num for num in range(second[0], second[1] + 1)}

        if lap1.intersection(lap2):
            count += 1

    return count


def main():
    with open("input.txt") as f:
        lines = f.readlines()
    # q1(lines)
    print(q2(lines))


if __name__ == "__main__":
    main()
