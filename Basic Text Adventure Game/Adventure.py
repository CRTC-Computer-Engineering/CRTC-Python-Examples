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

def main_menu():
    while(True):
        print("Welcome to the main menu\n[N] to start a new game, [L] to load an old one.")
        menu_input = (input(":")).upper() # Get the menu input and make it uppercase
        if menu_input == "N": # if the input is N
            menu_username = input("Input your name: ") # Ask for name
            global current_user # tell python that we're using the global instance of current_user
            current_user = "saves/" + menu_username + ".yaml" # Set the user to the user's file location
            save_userdata("name", menu_username)
            break
        elif menu_input == "L":
            print("Feature not functional")
        else:
            print("I did not understand that")

def save_userdata(data_type, data):
    if current_user == "":
        print("Error, you must create a user")
    else:
        try:
            current_user_data = enter_room(current_user)
            current_user_data.update({data_type: data})
            save_data(current_user, current_user_data)
        except:
            userfile = open(current_user, "w")
            userfile.write("name:")
            userfile.close()
            current_user_data = enter_room(current_user)
            current_user_data.update({data_type: data})
            save_data(current_user, current_user_data)

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
            
            elif (fuzzy_words(user_arg_2, ["UP", "ABOVE"])):
                selected_direction = 'up'
                try:
                    print(current_room['up']['desc'])
                except:
                    print("There is nothing above you")
                    
            elif (fuzzy_words(user_arg_2, ["DOWN", "BELOW"])):
                selected_direction = 'down'
                try:
                    print(current_room['down']['desc'])
                except:
                    print("There is nothing below you")
            
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
                print("Even i dont know where you are")
        elif (fuzzy_words(user_arg_1, ["INSPECT", "EXAMINE"])):
            try:
                print(current_room[selected_direction][user_arg_2.lower()]['inspect']) # Print the inspection text for that object
            except:
                print("This object cannot be inspected") # Tell the user that there is no information for that selected object
        elif (fuzzy_words(user_arg_1, ["PICKUP", "GRAB", "TAKE"])):
            print(current_room[selected_direction][user_arg_2.lower()]['desc'])
            print("pickup")
        elif (fuzzy_words(user_arg_1, ["EXIT", "MENU"])):
            save_userdata("current_room", current_yaml) # Save current room
            save_userdata("selected_direction", selected_direction) # Save current direction
            main_menu()
        elif (fuzzy_words(user_arg_1, ["USE"])):
            print("use")
        elif (fuzzy_words(user_arg_1, ["OPEN"])):
            if user_arg_2 == "DOOR":
                if selected_direction != '':
                    destination = current_room[selected_direction][user_arg_2.lower()]['dest']
                else:
                    print("You were not looking in a direction.")
                    destination = "Nowhere"
                if destination != "Nowhere":
                    confirm = (input(destination + ", would you like to enter? Y/N: ")).upper()
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
                print("This is not a door or cannot be opened")
        else:
            print("Thats not something I understand")
