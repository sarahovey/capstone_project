from Room import Room

class Kitchen(Room):
    def __init__(self):
        self.connected_rooms = self.load_connected_rooms()
        self.items = self.load_items()
        self.npcs = ""
        
    def load_connected_rooms(self):
        #Connected to
        #living room
        self.connected_rooms = []
        
    def load_items(self):
        self.items = []
        
    def load_npcs(self):
        self.npcs = []
        