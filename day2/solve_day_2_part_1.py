score = 0

# load the file
with open("input", "r") as input:
    # loop through the file
    lines = input.readlines()
    for new_line in lines:
        opponent, me = new_line.split()
        if me == "X":
            score += 1
            if opponent == "A":
                score += 3
            elif opponent == "B":
                score += 0
            elif opponent == "C":
                score += 6
            else:
                print("This should never happen.")
        elif me == "Y":
            score += 2
            if opponent == "A":
                score += 6
            elif opponent == "B":
                score += 3
            elif opponent == "C":
                score += 0
            else:
                print("This should never happen.")
        elif me == "Z":
            score += 3
            if opponent == "A":
                score += 0
            elif opponent == "B":
                score += 6
            elif opponent == "C":
                score += 3
            else:
                print("This should never happen.")
        else:
            print("This should never happen.")

# Get the total score
print(score)
