import rooms
import items
import npcs
import player

#this can be abstracted out later
class Phase1:
    def __init__(self):
        self.name = "Phase 1"
        self.player = ""
        self.make_player()
        self.rooms = self.make_rooms()
        
        
    def make_player(self):
        self.player = player.Player()
        
    def make_rooms(self):
        living_room = rooms.living_room(self.player)
        self.rooms = [living_room]
        self.player.change_room(living_room)
        print(self.player.current_room.name)
        self.player.current_room.enter_room()
        # kitchen = rooms.kitchen()
        # kitchen_door = items.door(self.player, "kitchen key", living_room, kitchen)
        # kitchen.doors = [kitchen_door]
        
        # back_yard = rooms.back_yard()
        # back_yard_door = items.door(self.player, "none", living_room, back_yard)
        # back_yard.doors = [back_yard_door]
        
        
        # bedroom = rooms.bedroom()
        # bedroom_door = items.door(self.player, "bedroom_key", living_room, bedroom)
        # bedroom.doors = [bedroom_door]
        
        # office = rooms.office()
        # office_door = items.door(self.player, "office key", living_room, office)
        # office.doors = [office_door]
        
        # self.rooms = [living_room, kitchen, back_yard, bedroom, office]
        
        
        