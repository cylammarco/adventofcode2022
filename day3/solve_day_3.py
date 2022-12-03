priority = 0

# load the file
with open("input", "r") as input:
    # loop through the file
    lines = input.readlines()
    # iterate through 3 items each time
    for new_line in zip(*[iter(lines)] * 3):
        # Remove end of line string
        elf_1 = set(list(new_line[0].strip()))
        elf_2 = set(list(new_line[1].strip()))
        elf_3 = set(list(new_line[2].strip()))
        mutual = list(elf_1.intersection(elf_2).intersection(elf_3))[0]
        temp = ord(mutual)
        # Get the priority for A to Z (upper case)
        if temp <= 90:
            priority += temp - 38
        # Get the priority for a to z (lower case)
        elif temp <= 122:
            priority += temp - 96
        else:
            print("This should never happen.")

print(priority)
