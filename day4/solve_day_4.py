counter_part_1 = 0
counter_part_2 = 0

# load the file
with open("input", "r") as input:
    # loop through the file
    lines = input.readlines()
    # iterate through the lines
    for new_line in lines:
        # Remove end of line string
        elf_1, elf_2 = new_line.split(",")
        elf_1_start, elf_1_end = elf_1.split("-")
        elf_2_start, elf_2_end = elf_2.split("-")
        elf_1_start = int(elf_1_start)
        elf_1_end = int(elf_1_end)
        elf_2_start = int(elf_2_start)
        elf_2_end = int(elf_2_end)
        # For part 1
        if (elf_1_start >= elf_2_start) and (elf_1_end <= elf_2_end):
            counter_part_1 += 1
        elif (elf_2_start >= elf_1_start) and (elf_2_end <= elf_1_end):
            counter_part_1 += 1
        else:
            pass
        # For part 2
        if (
            len(
                set(range(elf_1_start, elf_1_end + 1)).intersection(
                    set(range(elf_2_start, elf_2_end + 1))
                )
            )
            > 0
        ):
            counter_part_2 += 1
        else:
            pass

# answer for part 1
print(counter_part_1)

# answer for part 2
print(counter_part_2)
