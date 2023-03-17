import numpy as np

# Part 1
# load the file
lines = []
with open("input", "r") as input:
    # loop through the file
    for line in input.readlines():
        lines.append(list(line.strip("\n")))

lines = np.array(lines).astype("int")
visible = np.zeros_like(lines, dtype="bool")


# from left to right
for l, v in zip(lines, visible):
    v[0] = True
    vmax = l[0]
    for i in range(1, len(l)):
        if l[i] > vmax:
            vmax = l[i]
            v[i] = True


# from right to left
for l, v in zip(lines, visible):
    v[-1] = True
    vmax = l[-1]
    for i in range(len(l) - 2, 0, -1):
        if l[i] > vmax:
            vmax = l[i]
            v[i] = True

# rotate by 90 degrees:
lines = np.rot90(lines)
visible = np.rot90(visible)

# from left to right
for l, v in zip(lines, visible):
    v[0] = True
    vmax = l[0]
    for i in range(1, len(l)):
        if l[i] > vmax:
            vmax = l[i]
            v[i] = True


# from right to left
for l, v in zip(lines, visible):
    v[-1] = True
    vmax = l[-1]
    for i in range(len(l) - 2, 0, -1):
        if l[i] > vmax:
            vmax = l[i]
            v[i] = True

# part 1 answer
print(np.sum(visible))
