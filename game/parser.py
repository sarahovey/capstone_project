"""
import files
"""
import rooms
import phase
import npcs
import items

# command = input().split(" ")

# if command >= 4:
#     print("You don't know what you're doing.")

# if command >= 3:
#     if command in items

# if command >= 2:
#     if 

words = "here are words"

words = words.split

print("What will you do?")
command = input()

command = command.split()

if len(command) > 4:
    print("Too many!")

elif len(command) == 4:
    print("you tried too hard.... and fell over!")

elif len(command) == 3:
    action = command[0]
    #range in for loop needs a slice notation that works to capture past the index of zero other wise eat will repeat twice
    #I got the above but its missing the "a" in "eat a squirrel"
    for word in range(len(command)):
        obj = command[word] + " "
        
    print("action:") 
    print(action)
    print("object: " )
    print(obj)

elif len(command) == 2:
    action = command[0]
    for word in range(len(command)):
        obj = command[word]
    print("action:")
    print(action)
    print("object:")
    print(obj)

elif len(command) == 1:
    action = command[0]
    print("action:")
    print(action)
    
#     game.player_interact(action, obj)
    
# elif len(command) == 2:
#     #stuff i guess
    
# elif len(command) == 1:
#     game.player_action(command)
