#Item parent class
class Action:
    def __init__(self, name):
        self.name = name
    
    def description(self):
        if self.touched is False:
            print("unaltered")
        elif self.touched is True:
            print("altered")
            
    def interact(self):
        if self.touched:
            print("altered")
        else:
            print("unaltered")

class bite(Action):
        def __init_(self):
        self.name = "bite"
        # self.can_be_held = Falsex]
        self.touched = False
    def description(self):
        if self.touched is False:
            return "you bite!"
        else self.touched is True:
            return "you bit someone
#rand() number to generate a number to do damage
#fend off some bad guy in the game