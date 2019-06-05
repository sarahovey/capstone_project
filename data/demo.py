import rooms
import items
import phase
import npcs
import initializer
import test_parser

initializer = initializer.initializer()
parser = initializer.parser

print("done initializing in demo")
while(1):
    print("\nwhat do you do?")
    command = input()
    parser.parse(command)
    
    