class NPC:
    def __init__(self):
        self.name = ""
        self.met = False
        
class cat(NPC):
    def __init__(self):
        self.name = "cat"
        self.description = self.build_description()
        self.dialogue = self.show_dialogue()
        
    def meet(self):
        #call this when the player meets the npc
        #this way dialogue and description can
        #update accordingly
        self.met = True
        
    def build_description(self):
        #description can depend on whether or not you've already met the npc
        if self.met:
            print("its your old friend")
        else:
            print("You see your old friend, a big gray cat.")
        
    def show_dialogue(self):
        #check whether or not a player has a certain item
        #or has done something for the npc
        #or something else
        #that can change dialogue
        print ("mrowww")