import yaml
import Levenshtein as lev

select_edits = 2 # How close an input has to be to match
current_yaml = "gamedata/lobby.yaml"

selected_direction = ''
current_user = ""

def fuzzy_words(input_word, alisis_list):
    output = 0
    for word in alisis_list:
        if ((lev.distance(input_word, word)) < select_edits):
            output = output + 1
    if output >= 1:
        return True
    else:
        return False

def enter_room(filepath):
    """Reads data from a yaml file"""
    with open(filepath, "r") as file_desc:
        data = yaml.full_load(file_desc)
    return data

def save_data(filepath, data):
    """Dumps data to a yaml"""
    with open(filepath, "w") as file_desc:
        yaml.dump(data, file_desc)
    
def save_userdata(data_type, data):
    print(current_user)
    if current_user == "":
        print("Error, you must create a user")
    else:
        current_user_data = enter_room(current_user)
        current_user_data.update([data_type][data])
        save_data(current_user, current_user_data)
        
def main_menu():
    print("Welcome to the main menu\n[N] to start a new game, [L] to load an old one.")
    menu_input = (input(": ")).upper()
    if menu_input == "N":
        menu_username = input("Input your name: ")
        current_user = "saves/" + menu_username + ".yaml"
        print(current_user)
        save_userdata("name", menu_username)
    elif menu_input == "L":
        print("Feature not functional")

if __name__ == "__main__": # If this is the main file
    current_room = enter_room(current_yaml) # fill current_room with all the room data of the current room 
    main_menu()
    print (current_room['roommeta']['desc']) # give us the desc of that room
    while(True):
    
        user_command = (input(":")).upper()
        user_arg_1 = user_command.split()[0]
        try:
            user_arg_2 = user_command.split()[1]
        except:
            user_arg_2 = ""
        
        if (fuzzy_words(user_arg_1, ["LOOK"])):
            if (fuzzy_words(user_arg_2, ["LEFT"])):
                selected_direction = 'left'
                try:
                    print(current_room['left']['desc'])
                except:
                    print("There is nothing notible to your left")
                    
            elif (fuzzy_words(user_arg_2, ["RIGHT"])):
                selected_direction = 'right'
                try:
                    print(current_room['right']['desc'])
                except:
                    print("There is nothing notible to your right")
                    
            elif (fuzzy_words(user_arg_2, ["AHEAD", "FORWARD"])):
                selected_direction = 'ahead'
                try:
                    print(current_room['ahead']['desc'])
                except:
                    print("There is nothing ahead of you")
                
            elif (fuzzy_words(user_arg_2, ["BEHIND", "BACK"])):
                selected_direction = 'behind'
                try:
                    print(current_room['behind']['desc'])
                except:
                    print("Missing Data")
        elif (fuzzy_words(user_arg_1, ["WHERE", "MAP"])):
            try:
                print(current_room[selected_direction])
            except:
                print("Choose a direction")
        elif (fuzzy_words(user_arg_1, ["INSPECT", "EXAMINE"])):
            print(current_room[selected_direction][user_arg_2.lower()]['inspect'])
        elif (fuzzy_words(user_arg_1, ["PICKUP", "GRAB"])):
            print("pickup")
        elif (fuzzy_words(user_arg_1, ["EXIT", "MENU"])):
            main_menu()
        elif (fuzzy_words(user_arg_1, ["OPEN"])):
            if user_arg_2 == "DOOR":
                destination = current_room[selected_direction][user_arg_2.lower()]['dest']
                if destination != "Nowhere":
                    confirm = input(destination + ", would you like to enter? Y/N: ")
                    if confirm == "Y":
                        current_yaml = current_room[selected_direction][user_arg_2.lower()]['path']
                        current_room = enter_room(current_yaml)
                        print (current_room['roommeta']['desc'])
                    elif confirm == "N":
                        break
                    else:
                        print("I did not understand the command")
                else:
                    print("This door does not lead anywhere, its a wonder somebody took the time to install it.")
            else:
                print("This is not a door")
        else:
            print("Thats not something I understand")