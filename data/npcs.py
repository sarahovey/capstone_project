class NPC:
    def __init__(self):
        self.name = ""
        self.met = False
        
#Ideally we'd have these completely abstracted out,
#but we have so few npcs that it doesn't matter too much
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
        
class rusty(NPC):
    def __init__(self):
        self.name = "Rusty"
        self.description = self.build_description()
        self.dialogue = self.show_dialogue()
        self.met = False
        self.quest_finished = False 
        
    def meet(self):
        #call this when the player meets the npc
        #this way dialogue and description can
        #update accordingly
        self.met = True
        
    def build_description(self):
        #description can depend on whether or not you've already met the npc
        if self.met:
            print("It's Rusty, your new friend")
        else:
            print("Another Cattle Dog, big and red. Maybe a new friend?")
        
    def is_quest_finished(self):
        #Check if the player has the npc's requested item in their inventoru
        
    def show_dialogue(self):
        #check whether or not a player has a certain item
        #or has done something for the npc
        #or something else
        #that can change dialogue
        if self.met:
            if self.is_quest_finished():
                print("")
            else:
                print("")
        else:
            print("Hi new friend! I'm Rusty. I like hanging out in this park and chewing on sticks")
            print("")