# needs an "invalid entry" option....
print("""
Use this calculator to determine how many total reps you are
doing of an exercise if you reduce your count by 1 each set.
Enter "quit" to exit.""")
while True:
    command = input("\nHow many reps to start? Enter a number: ")
    if command.lower() == "quit":
        break
    else:
        starting_reps = int(command)
        total_no_reps = (1 + starting_reps)*(starting_reps/2)
        print(f"{int(total_no_reps)} total reps")
