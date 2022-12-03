# empty dictionary to load the Calories of each elf's found
input_data = {}
i = 1

# load the file
with open("input", "r") as input:
    # loop through the file
    lines = input.readlines()
    for new_line in lines:
        # if not a new line, add to the same elf
        if new_line != "\n":
            if i in input_data.keys():
                input_data[i] += int(new_line)
            else:
                input_data[i] = int(new_line)
        else:
            i += 1


# Part 1
# Get the maximum Calories
print(max(input_data.values()))

# Part 2
# Get the total Calories of the top 3
print(sum(sorted(input_data.values())[-3:]))
