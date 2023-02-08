##############################
##    Variables - Game State 
##############################

game = {"tool": 0, "money": 0}

tools = [
    {"name": "teeth", "profit": 1, "cost": 0},
    {"name": "rusty scissors", "profit": 5, "cost": 5},
    {"name": "old-timey lawn mower", "profit": 50, "cost": 25},    
    {"name": "battery powered lawn mower", "profit": 100, "cost": 250},
    {"name": "team", "profit": 250, "cost": 500}                 
]

## Game Option Funtion

def cut_lawns():
    tool = tools[game["tool"]]
    game["money"] += tool["profit"]
    print(f"You cut lawns using your {tool['name']} and are making ${tool['profit']}")
    

def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have ${game['money']} and are using {tool['name']}")

def upgrate():
    if (game["tool"] >= (len(tools) -1)):
        print("No more upgrades")
        return 0
    next_tool = tools[game["tool"] + 1]
    if (next_tool == None):
        print("There is no more tools")
        return 0
    if (game["money"] < next_tool["cost"]):
        print("not enough money to buy this tool")
        return 0
    print("You are upgrading your tool")
    # update game money
    game["money"] -= next_tool["cost"]
    # update game tool
    game["tool"] += 1

def win_check():
    if (game["tool"] == 4 and game["money"] >= 1000):
        print("You win")
        return True
    return False

while(True):
    
    i = input("[1] Cut Lawn [2] Check Stats [3] Upgrate [4] Quit")
    
    i = int(i)
    
    if (i == 1):
        cut_lawns()
    
    if (i == 2):
        check_stats()
    
    if (i == 3):
        upgrate()
    
    if (i == 4):
        print("You quit the game")
        break
    if (win_check()):
        break

