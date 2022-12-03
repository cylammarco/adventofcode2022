score = 0

# load the file
with open("input", "r") as input:
    # loop through the file
    lines = input.readlines()
    for new_line in lines:
        opponent, me = new_line.split()
        if me == "X":
            score += 0
            # Rock
            if opponent == "A":
                score += 3
            # Paper
            elif opponent == "B":
                score += 1
            # Scissors
            elif opponent == "C":
                score += 2
            else:
                print("This should never happen.")
        elif me == "Y":
            score += 3
            # Rock
            if opponent == "A":
                score += 1
            # Paper
            elif opponent == "B":
                score += 2
            # Scissors
            elif opponent == "C":
                score += 3
            else:
                print("This should never happen.")
        elif me == "Z":
            score += 6
            # Rock
            if opponent == "A":
                score += 2
            # Paper
            elif opponent == "B":
                score += 3
            # Scissors
            elif opponent == "C":
                score += 1
            else:
                print("This should never happen.")
        else:
            print("This should never happen.")

# Get the total score
print(score)
