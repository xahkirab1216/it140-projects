"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

current_room = 'Great Hall'

while True:
    print('You are in', current_room)

    command = input('Enter your move:\n')

    if command.lower() == 'exit':
        print('Thanks for playing!')
        break

    command = command.split()

    if len(command) == 2 and command[0].lower() == 'go':
        direction = command[1].capitalize()

        if direction in rooms[current_room\]:
            current_room = rooms[current_room][direction]
    else:
        print("You can't go that way.")

# TODO: Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
#   1. Display the current room.
#   2. Prompt for a movement command or "exit".
#   3. Branch for a valid move, exit, or invalid input.
#   4. Update the room only after a valid movement command.
#   5. Continue until the required exit condition is reached.

# TODO: Run and debug all milestone cases in prototype/README.md.
