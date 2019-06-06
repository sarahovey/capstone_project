import rooms
import items
import phase
import npcs
import initializer
import test_parser

initializer = initializer.initializer()
parser = initializer.parser

while(1):
    print("\nwhat do you do?")
    command = input()
    parser.parse(command)
    
    