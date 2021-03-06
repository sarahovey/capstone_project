import rooms
class Player:
    def __init__(self):
        self.name = "player"
        self.inventory = []
        self.current_room = None
        
    def look_around(self):
        self.current_room.long_description()
        
    def look_at(self, item):
        item.description()
        
    def go(self, landmark):
        if landmark.name == "door" or landmark.name == "gate":
            landmark.change_room()
        else:
            landmark.description()
        
    def doors(self):
        print("You are in " + self.current_room)
        for door in self.current_room:
            print("There is a door between " + door.from_room + " and " + door.to_room + "\n")
        
    def check_inventory(self):
        if len(self.inventory) == 0:
            print("Your saddlebags are empty!")
            return
            
        print("You check in your saddlebags and see")
        for item in self.inventory:
            print("\t- " + item.name + ". " + str(item.description()))
            
    def help(self):
        filepath = 'help.txt' 
        with open(filepath) as fp: 
            for line in fp:
                print(line)

    #Get a list of item names (strings) to see if the player has one or mroe in inventory
    def find_item(self, items):
        for item in self.inventory:
            if item.name in items:
                return True
            else:
                return False
    def quit(self):
        quit = None
        while quit is None:
            print("are you sure? y/n")
            command = input()
            if command == 'y':
                exit()
            elif command == 'n':
                return
            else:
                print("try y or n ")
        
    def change_room(self, new_room):
        self.current_room = new_room
        self.current_room.enter_room()
        
    #Single word actions
    def action(self, action):
        if action == "look":
            self.look_around()
        elif action == "inventory":
            self.check_inventory()
        elif action == "help" :
            self.help()
        elif action == "exit" or action == "quit":
            self.quit()
        else:
            print("you tried to hard...")
               
    #Interaction with an npc
    def interact_npc(self, npc):
        if len(self.current_room.npcs) >= 1: 
            for person in self.current_room.npcs:
                if person.name == npc:
                    person.interact()
                    return
            #here we can assume that no npc by that name was found
            print("That person isn't in here!")
            
        else:
            print("There's no one here....")
          
    #Interaction with a door, trying to enter, unlock, etc      
    def interact_door(self, target_door):
        #print("on the player, the door is " + target_door)
        #Phase 1 and 3 doors
        if hasattr(self.current_room, 'doors'):

            #there is only one occasion of a phase door being put into the doors list in a room
            
            #BUGS HERE with print stuck in for loop
            for door in self.current_room.doors:

                #this supports just the name of the room, we'd need to strip "door" 
                #out in the parser from the end of a command, unless its 'front door'
                if hasattr(door, 'to_room' ):
                    if door.to_room.name == target_door:
                        door.interact()
                        return
                    elif door.from_room.name == target_door:
                        door.interact()
                        return
                    else:
                        # print("I don't think that's a door...")
                        pass
                        
                #this is always the front door in phase 1
                elif hasattr(door, 'to_phase'):
                    if door.name == target_door:
                        door.interact()
                        return
                        
        #Phase 2 gates
        if hasattr(self.current_room, 'gates'):
            for gate in self.current_room.gates:
                if hasattr(gate, 'to_room' ):
                    if gate.to_room.name == target_door:
                        gate.interact()
                        return
                    elif gate.from_room.name == target_door:
                        gate.interact()
                        return
                    else:
                        pass
                        # print("bad door")
                        # print("I don't think that's a door...")
            
        print("That's not a room you can go into!")
        
    #Dropping or using an item in inventory    
    def interact_inventory(self, action, obj):
        if action == "drop":
            #check inventory for the item to drop
            # if obj in self.inventory:
            for item in self.inventory:
                if item.name == obj:
                    self.inventory.remove(item)
                    self.current_room.items.append(item)
                    print("you dropped " + item.name)
                    return
                
                print("That item isn't in your inventory, you can't use or drop it!")

        #use an inventory item, 
        #just print the desc if it exists
        elif action == "use":
            for item in self.inventory:
                if item.name == obj:
                    item.interact()
                    return
            print("That item isn't in your inventory, you can't use or drop it!")
            
        else:
            print("That item isn't in your inventory, you can't use or drop it!")
        
    #Interacting with an item in the room
    def interact_item(self, action, obj):
        found_action = False
        found_item = False
        target_item = None
        for item in self.current_room.items:
            #Look for the item in the current room
            if item.name == obj:
                #We have found the item by name in the room
                found_item = True
                target_item = item
                
                #Try taking an item
                if action == "take":
                    if item.can_be_held is True:
                        self.inventory.append(item)
                        self.current_room.items.remove(item)
                        print("You added the item to your inventory~")
                        found_action == True
                        #found_item == False
                    else:
                        print("You can't hold that! >:(")
                    return
                        
       #We can assume that the item does not exist in the room
        if found_item is False: #and found_action is not False:
            print("that's not a real thing!")
            return
        
        #Once we have found the item, we can see if it has that action on it
        for word in target_item.actions:
            if word == action:
                target_item.interact()
                found_action == True
                return
                #found_item = False
                    
        #we can assume that that action does not apply to the item that was found
        if found_action is False and found_item is not False:
            print("You can't doooo that!")
                        
        
        
        