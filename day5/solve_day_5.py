import copy

crates = []
moves = []
ship = {}

this_is_crate = True

# load the file
with open("input", "r") as input:
    # loop through the file
    lines = input.readlines()
    # iterate till it hits a blank line
    for new_line in lines:
        if new_line == "\n":
            this_is_crate = False
            continue
        # crate info
        if this_is_crate:
            crates.append(new_line)
        # movement info
        else:
            moves.append(new_line)

# 'Rotate' the text and 'move' them to the ship as a dictionary of list
# The end of the list is the top of the stack of crates
rotated_crates = ["".join(reversed(a)) for a in zip(*crates)]
for i in rotated_crates:
    if i[0].isnumeric():
        ship[int(i[0])] = list(i[1:].strip())


ship_1 = copy.deepcopy(ship)
ship_2 = copy.deepcopy(ship)

# loop through the movements
for m in moves:
    n, from_stack, to_stack = [int(s) for s in m.split() if s.isdigit()]
    for i in range(n):
        ship_1[to_stack].extend(ship_1[from_stack].pop())

# answer for part 1
answer_1 = []
for i in ship_1.keys():
    answer_1.append(ship_1[i][-1])

print("".join(answer_1))


# loop through the movements
for m in moves:
    n, from_stack, to_stack = [int(s) for s in m.split() if s.isdigit()]
    temp = []
    for i in range(n):
        temp.append(ship_2[from_stack].pop())
    ship_2[to_stack].extend(copy.deepcopy(temp[::-1]))

# answer for part 2
answer_2 = []
for i in ship_2.keys():
    temp_crates = ship_2[i]
    if temp_crates != []:
        answer_2.append(temp_crates[-1])
    else:
        answer_2.append(" ")

print("".join(answer_2))
