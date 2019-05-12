import rooms
import items
import phase
import npcs
import initializer

initializer = initializer.initializer()
choice = input()
current_phase = ""
game_type = False

while game_type is False:
    if choice == "1":
        current_phase = initializer.load_game(choice)
        game_type == True
        break
    elif choice == "2":
        print("No game to load, try starting a new one")
        break
    else:
        print("try again")
        break
    
#current_phase.player.current_room
#start whole input loop

# while(1):
#     print("What will you do?")
    