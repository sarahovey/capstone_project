class Parser:
    def __init__(self, game):
        self.game = game
        
    def parse(self, command):
        command = command.split()
        door_words = ['open', 'unlock', 'enter', 'go to']
        #This probably wants refactoring...
        
        if len(command) > 4:
            print("Too many words, you've never been great with words")
        
        elif len(command) == 4:
            if command[0] == "take":
                action = "take"
                item = command[1] + " " + command[2] + " " + command[3]
                self.game.player_item_interaction(action, item)
            elif command[0] in door_words or command[0] + " " + command[1] in door_words:
                door=command[2] + " " + command[3]
                self.game.player_door_interaction(door)
                
            elif command[0] == "look" and command[1] == "at":
                item = command[2] + " " + command[3]
                action = command[0] + " " + command[1]
                self.game.player_item_interaction(action, item)
                
            else:
                print("You tried.... but made a loud bork instead")
                
            
        elif len(command) == 3:
            #if the first two words in a 3 word command are "talk to"
            if command[0] == "talk" and command[1] == "to":
                npc = command[2]
                #print(npc)
                self.game.player_npc_interaction(npc)
                
            #if the first word in a 3 word command is "drop" or "use"
            elif command[0] == "drop" or command[0] == "use":
                action = command[0]
                item = command[1] + " " + command[2]
                self.game.player_inventory_interaction(action, item)
                
            #if the first word in a 3 word command is "open", "unlock", or "enter"
            elif command[0] in door_words or command[0] + " " + command[1] in door_words:
                #do we need the full phrase? like 'kitchen door' or just 'kitchen'?
                #we should be checking to see if the last word is 'door' and maybe get rid of that?
                door=command[1] + " " + command[2]
                self.game.player_door_interaction(door)
                
            elif command[0] == "look" and command[1] == "at":
                item = command[2]
                action = command[0] + " " + command[1]
                self.game.player_item_interaction(action, item)
                
            else:
                #2+ word command to interact with an item
                action = command[0]
                item = command[1] + " " + command[2]
                #print(item)
                self.game.player_item_interaction(action, item)
          
        elif len(command) == 2:
            #if the first word in a 2 word command is "open", "unlock", or "enter"
            if command[0] in door_words:
                door= command[1]
                self.game.player_door_interaction(door)
                
            #if the first word in a 2 word command is "drop" or "use"
            elif command[0] == "drop" or command[0] == "use":
                action = command[0]
                item = command[1]
                self.game.player_inventory_interaction(action, item)
                  
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
  