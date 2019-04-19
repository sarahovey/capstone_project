from Room import Room

class LivingRoom(Room):
    def __init__(self):
        self.connected_rooms = self.load_connected_rooms()
        self.items = self.load_items()
        self.npcs = ""
        
    def load_connected_rooms(self):
        #Connected to
        #kitchen
        #office
        #back yard
        #bedroom
        self.connected_rooms = []
        
    def load_items(self):
        self.items = []
        
    def load_npcs(self):
        self.npcs = []
        
    def enter_room(self):
        #set the enter flag
        #check for any conditional npcs, items, etc
        
        print("you entered room")