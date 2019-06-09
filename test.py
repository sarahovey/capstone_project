#import game
#game = game.game()

words = "here are words"

words = words.split

print("What will you do?")
command = input()

command = command.split()

#This probably wants refactoring...
if len(command) > 3:
    print("too many!")
elif len(command) == 3:
  #if the first two words in a 3 word command are "talk to"
  if command[0] == "talk" and command[1] == "to":
      npc = command[2]
      print(npc)
      #game.player_npc_interaction(npc)
      
  #if the first word in a 2+ word command is "drop" or "use"
  if command[0] == "drop" or command[0] == "use":
      item = command[1] + " " + command[2]
      print(item)
      #game.player_inventory_interaction(item)
   
  #if the first word in a 2+ word command is "open", "unlock", or "enter"
  door_words = ['open', 'unlock', 'enter']
  if command[0] in door_words:
      door=command[1] + " " + command[2]
      print(door)
           
  #2+ word command to interact with an item
  action = command[0]
  item = command[1] + " " + command[2]
  print(item)
  #game.player_item_interaction(action, item)
  
elif len(command) == 2:
    #if the first word in a 2+ word command is "open", "unlock", or "enter"
    door_words = ['open', 'unlock', 'enter']
    for word in door_words:
      if command[0] == word:
          door="Make the 2nd and 3rd words into a string here,'kitchen', 'door' should be 'kitchen door'"
          #game.player_door_interaction(door)
    #2+ word command to interact with an item
    
elif len(command) == 1:
    #1 word commands, like help or inventory 
    #game.player_action(command[0])
    print(command)