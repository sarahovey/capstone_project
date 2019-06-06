import rooms
import items
import npcs
import player

#this can be abstracted out later
class Phase1:
    def __init__(self, player):
        self.name = "Phase 1"
        self.player = player
        self.spawn_point = ""
        self.rooms = []
        self.make_rooms()
        
        
    def start_phase(self):
        #set current phase and room
        self.player.current_phase = self
        self.player.current_room = self.spawn_point

        #show game starting text
        filepath = 'data/phase1_starting_flavor.txt' 
        with open(filepath) as fp: 
            for line in fp:
                print(line)
                input()
                
        self.player.current_room.enter_room()
        
    def make_rooms(self):
        living_room = rooms.living_room(self.player)
        self.rooms = [living_room]
        #self.player.current_room.enter_room()
        
        kitchen = rooms.kitchen(self.player)
        kitchen_door = items.door(self.player, "kitchen key", living_room, kitchen)
        kitchen.doors = [kitchen_door]
        
        back_yard = rooms.back_yard(self.player)
        back_yard_door = items.door(self.player, "none", living_room, back_yard)
        back_yard.doors = [back_yard_door]
        
        
        bedroom = rooms.bedroom(self.player)
        bedroom_door = items.door(self.player, "bedroom key", living_room, bedroom)
        bedroom.doors = [bedroom_door]
        
        office = rooms.office(self.player)
        office_door = items.door(self.player, "office key", living_room, office)
        office.doors = [office_door]

        #make sure doors can handle room changes
        
        living_room.doors = [kitchen_door, back_yard_door, bedroom_door, office_door]
        
        self.rooms = [living_room, kitchen, back_yard, bedroom, office]
        self.spawn_point = living_room
        
        
class Phase2:
    def __init__(self, player):
        self.name = "Phase 2"
        self.player = player
        self.rooms = []
        self.make_rooms()
        self.spawn_point = ""
        
        
    def start_phase(self):
        #set current phase and room
        self.player.current_phase = self
        self.player.current_room = self.spawn_point

        #show game starting text
        filepath = 'data/phase2_starting_flavor.txt' 
        with open(filepath) as fp: 
            for line in fp:
                print(line)
                input()
                
    def make_rooms(self):
        open_grass = rooms.open_grass(self.player)
        
        sand_pit = rooms.sand_pit(self.player)
        sand_pit_gate = items.gate(self.player, sand_pit, open_grass)
        sand_pit.gates = [sand_pit_gate]
        
        agility_course = rooms.agility_course(self.player)
        agility_course_gate = items.gate(self.player, agility_course, open_grass)
        agility_course.gates = [agility_course_gate]
        
        dog_pool = rooms.dog_pool(self.player)
        dog_pool_gate = items.gate(self.player, dog_pool, open_grass)
        dog_pool.gates = [dog_pool_gate]
        
        shady_grove = rooms.shady_grove(self.player)
        shady_grove_gate = items.gate(self.player, shady_grove, open_grass)
        shady_grove.gates = [shady_grove_gate]
        
        
        open_grass.gates = [sand_pit_gate, agility_course_gate, dog_pool_gate, shady_grove_gate]
        self.rooms = [open_grass, sand_pit, shady_grove, agility_course, dog_pool]
        self.spawn_point = open_grass
        
class Phase3:
    def __init__(self, player):
        self.name = "Phase 3"
        self.player = player
        self.rooms = []
        self.make_rooms()
        self.spawn_point = ""
        
    def start_phase(self):
        #set current phase and room
        self.player.current_phase = self
        self.player.current_room = self.spawn_point

        #show game starting text
        filepath = 'data/phase3_starting_flavor.txt' 
        with open(filepath) as fp: 
            for line in fp:
                print(line)
                input()
    def make_rooms(self):
        lobby = rooms.lobby(self.player)
        
        cubicle = rooms.cubicle(self.player)
        cubicle_door = items.gate(self.player, lobby, cubicle)
        cubicle.doors = [cubicle_door]
        
        break_room = rooms.break_room(self.player)
        break_room_door = items.gate(self.player, lobby, break_room)
        break_room.doors = [break_room_door]
        
        supply_closet = rooms.supply_closet(self.player)
        supply_closet_door = items.gate(self.player, lobby, break_room)
        supply_closet.doors = [supply_closet_door]
        
        common_area = rooms.common_area(self.player)
        common_area_door = items.gate(self.player, lobby, common_area)
        common_area.doors = [common_area_door]
        
        lobby_doors = [cubicle_door, break_room_door, supply_closet_door, common_area_door]
        self.rooms = [lobby, cubicle, break_room, supply_closet, common_area]
        self.spawn_point = lobby
        
        
        