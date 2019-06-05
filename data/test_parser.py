class Parser:
    def __init__(self, game):
        self.game = game
        
    def parse(self, command):
        command = command.split()
        door_words = ['open', 'unlock', 'enter']
        #This probably wants refactoring...
        if len(command) > 3:
            print("too many!")
            
        elif len(command) == 3:
            #if the first two words in a 3 word command are "talk to"
            if command[0] == "talk" and command[1] == "to":
                npc = command[2]
                #print(npc)
                self.game.player_npc_interaction(npc)
                
            #if the first word in a 2+ word command is "drop" or "use"
            elif command[0] == "drop" or command[0] == "use":
                item = command[1] + " " + command[2]
                #print(item)
                self.game.player_inventory_interaction(item)
                
            #if the first word in a 2+ word command is "open", "unlock", or "enter"
            elif command[0] in door_words:
                print("Door command!!")
                print(command[0])
                #do we need the full phrase? like 'kitchen door' or just 'kitchen'?
                #we should be checking to see if the last word is 'door' and maybe get rid of that?
                door=command[1] + " " + command[2]
                print(door)
                self.game.player_door_interaction(door)
                
            else:
                #2+ word command to interact with an item
                action = command[0]
                item = command[1] + " " + command[2]
                #print(item)
                self.game.player_item_interaction(action, item)
          
        elif len(command) == 2:
            #if the first word in a 2+ word command is "open", "unlock", or "enter"
            if command[0] in door_words:
                door= command[1]
                self.game.player_door_interaction(door)
                  
            else:
                #2+ word command to interact with an item, like 'bite hose'
                action = command[0]
                item = command[1]
                #print("You said: " + item)
                self.game.player_item_interaction(action, item)
            
        elif len(command) == 1:
            #single word actions, like 'help' or 'inventory'
            self.game.player_action(command[0])
            
        else:
            print("ahhhh")
  