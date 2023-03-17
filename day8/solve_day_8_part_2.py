import numpy as np
import itertools

# Part 1
# load the file
lines = []
with open("input", "r") as input:
    # loop through the file
    for line in input.readlines():
        lines.append(list(line.strip("\n")))

lines = np.array(lines).astype("int")


max_score = 0

for i, j in itertools.product(np.arange(len(lines)), np.arange(len(lines[0]))):
    score = 0
    val = lines[i][j]
    left = 0
    right = 0
    top = 0
    bottom = 0
    if i > 0:
        for _i1 in range(i - 1, -1, -1):
            if lines[_i1][j] < val:
                left += 1
            else:
                left += 1
                break
    if i < len(lines):
        for _i2 in range(i + 1, len(lines)):
            if lines[_i2][j] < val:
                right += 1
            else:
                right += 1
                break
    if j > 0:
        for _j1 in range(j - 1, -1, -1):
            if lines[i][_j1] < val:
                top += 1
            else:
                top += 1
                break
    if j < len(lines):
        for _j2 in range(j + 1, len(lines)):
            if lines[i][_j2] < val:
                bottom += 1
            else:
                bottom += 1
                break
    score = left * right * top * bottom
    if score > max_score:
        max_score = score


print(max_score)
