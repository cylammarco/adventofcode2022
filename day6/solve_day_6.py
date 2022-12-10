# Part 1
# load the file
with open("input", "r") as input:
    # loop through the file
    line = list(input.readline())
    for i in range(len(line) - 4):
        if len(set(line[i:i+4])) == 4:
            print(i + 4)
            break

# Part 2
with open("input", "r") as input:
    # loop through the file
    line = list(input.readline())
    for i in range(len(line) - 14):
        if len(set(line[i:i+14])) == 14:
            print(i + 14)
            break
