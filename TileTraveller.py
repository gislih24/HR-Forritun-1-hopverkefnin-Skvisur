from typing import Tuple
import os

# Constants
NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"
QUIT = "quit"

STARTING_LOCATION = (1, 1)
FINAL_DESTINATION = (3, 1)
SAVE_PATH = "saved_games.txt"


def main():
    location_tuple = STARTING_LOCATION
    while location_tuple != FINAL_DESTINATION:
        location_tuple = play_one_move(location_tuple)

        if os.path.exists(SAVE_PATH):
            print("Save file found, writing to it...")
            with open(file=SAVE_PATH, mode="a") as file:
                file.write(str(location_tuple) + "\n")
        else:
            print("No pre-existing save file found, creating new save file...")
            with open(file=SAVE_PATH, mode="w") as file:
                file.write(str(location_tuple) + "\n")
        file.close()

    print("Victory!")
    # Example of creating a file in Python


def play_one_move(location: Tuple[int, int]) -> Tuple[int, int]:
    """Plays one move of the game.

    Returns updated location.
    """

    valid_directions_str_tuple = find_directions(location)
    direction: str = get_direction(valid_directions_str_tuple)

    if direction == QUIT:
        print("bla")
        exit(0)

    elif direction in valid_directions_str_tuple:
        location = move(direction, location)
    else:
        print("Not a valid direction!")

    return location


def find_directions(location: Tuple[int, int]) -> Tuple[str, ...]:
    """Returns valid directions as a string given the supplied location."""

    if location == (1, 1):
        valid_directions_str_tuple = (NORTH,)
    elif location == (1, 2):
        valid_directions_str_tuple = NORTH, EAST, SOUTH
    elif location == (1, 3):
        valid_directions_str_tuple = EAST, SOUTH
    elif location == (2, 1):
        valid_directions_str_tuple = (NORTH,)
    elif location == (2, 2):
        valid_directions_str_tuple = SOUTH, WEST
    elif location == (2, 3):
        valid_directions_str_tuple = EAST, WEST
    elif location == (3, 2):
        valid_directions_str_tuple = NORTH, SOUTH
    elif location == (3, 3):
        valid_directions_str_tuple = SOUTH, WEST

    return valid_directions_str_tuple


def get_direction(valid_directions: Tuple[str, ...]) -> str:
    while True:
        print_directions(valid_directions)
        direction = input("Direction (or 'quit' to quit): ")
        if direction == QUIT:
            return QUIT
        elif direction in valid_directions:
            return direction
        else:
            print("Invalid direction! Please try again.")


def print_directions(available_directions: Tuple[str, ...]) -> None:
    print("You can travel: ", end="")

    one_done_already = False
    for direction in available_directions:
        if one_done_already:
            print(" or ", end="")

        if direction == NORTH:
            print("(N)orth", end="")
        elif direction == EAST:
            print("(E)ast", end="")
        elif direction == SOUTH:
            print("(S)outh", end="")
        elif direction == WEST:
            print("(W)est", end="")

        one_done_already = True

    print(".")


def move(direction: str, location: Tuple[int, int]) -> Tuple[int, int]:
    """Returns updated location given the direction."""

    x, y = location

    if direction == NORTH:
        y += 1
    elif direction == SOUTH:
        y -= 1
    elif direction == EAST:
        x += 1
    elif direction == WEST:
        x -= 1

    return x, y


if __name__ == "__main__":
    main()


# x = 0 # bæði initialized sem 0
# y = 0

# Erum með fall sem heitir : GetValidDirections() sem gefur okkur áttirnar sem er hægt að fara í (áttirnar eru hérna fyrir neðan :
# 1,1 ≡ 2,1 (↑N)
# 1,2 ≡ 3,2 (↑N,↓S)
# 2,2 ≡ 3,3 (←W,↓S)
# 1,3 (↓S,→E)
# 2,3 (←W,→E)
# Svo annað fall sem prentar þau á flottan hátt sem heitir PrintValidDirections() (notar gögn frá GetValidDirections().)

# Erum með annað fall sem færir playerinn (a.k.a. hækkar/lækkar x/y) sem heitir uhhhh “Move()”

# og Main(), of couuuuurse

# In this assignment we are going to focus on reading, writing and editing files. You can implement
# these features in any order that you choose and you can experiment as much as you like. Feel free
# to add more, change the features and be creative in the way you present the terminal user interface.
# 1. Make an extra option in the game which is “save”. This option, as well as “quit” can be
# chosen at any time, whether or not the game has been finished. If the user chooses to “save”
# the whole state of the game will be written into a file. Make sure all items, points and coins
# are saved if applicable.

# 2. Make an extra option in the game which is “load”. This option, as well as “quit” and “save” can
# be chosen at any time, whether or not the game has been finished. If the user chooses to
# “load” the whole state of the game will be read from the file that was saved and the current
# state loaded. The next choice menu displayed will be exactly as if the player was playing the
# same game as when they saved.

# 3. Change the “save” and “load” options so that you can save different save game files.
# When saving the user is asked to type a name for the saved game. When loading the user
# gets a list of all saved games and chooses one by entering an integer.
# One way to know which saved games exist is keeping one file that your program always
# knows the name of, e.g. “saved_games.txt”. In that file write the names of all the saved
# games. When the user loads, first read from that file and display the names of the games.
# When the user chooses, then you can take the correct filename and open the actual game file.

# 4. At some point it can be fun to add points or coins to some of the cells. You might add an
# option to the menu, “search” or the program might state “There are 2 coins in this room” and
# an option to pick them up. Use a variable to have a different number of coins in each room.
# Have fun with this “gamification”. Add up all the coins and show the player how many they
# have, or have an option “show points” or even “show inventory” and have more things that can
# be picked up :)

# 5. Build a high-score list that can be kept in a file and viewed at any time. Allow the user to play
# as many games as they like in a row, but keep track of the sum of points that they have
# collected throughout all the games, or the number of games finished if there are no points.
# When the user quits, ask them for their initials for the high score list.
# Keep all high scores in the list. Best implementation would be to keep them ordered, so that
# when you add a new high score, you add it in the correct location in the file. You can either
# insert into the file or you can read from the file and write back into it, making sure you enter
# the new score in the right place.

# Add the option “view high-score list” to the option menu for the user.
# Group members and fellow students should discuss what everything means in this assignment
# description and how it can be implemented. Make sure you have a fairly good idea of what is needed
# before you start, but also remember that many things will not be clear until you start experimenting in
# the programming environment.
