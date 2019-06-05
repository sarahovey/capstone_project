words = "here are words"

words = words.split

print("What will you do?")
command = input()

command = command.split()

#4 words:
#3 words: action with compount object; 'take tennis ball', 'talk to rusty', 'go to kitchen'
#edge case: if the first word is drop, search inventory
#if the first word is use, search inventory
#2 words: action with single object; 'bite rope'
#1 word: player action; inventory
if len(command) > 4:
    print("Too many!")
elif len(command) == 4:
    print("you tried too hard.... and fell over!")
elif len(command) == 3:
    #edge cases: 'talk to', and 'go to'
    action=command[0]
    for word in range(len(command)):
        action += command[word] + " "
        
    print("object: " )
    #print(obj)
    print("action:") 
    print(action)
    
    game.player_interact(action, obj)
    
elif len(command) == 2:
    #stuff i guess
    print("")
    
elif len(command) == 1:
    print("game.player_action(command)")