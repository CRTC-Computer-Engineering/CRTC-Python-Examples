import yaml
import Levenshtein as lev

select_edits = 2 # How close an input has to be to match
current_yaml = "gamedata/lobby.yaml"

selected_direction = ''

def enter_room(filepath):
    """Reads data from a yaml file"""
    with open(filepath, "r") as file_desc:
        data = yaml.full_load(file_desc)
    return data

def save_data(filepath, data):
    """Dumps data to a yaml"""
    with open(filepath, "w") as file_desc:
        yaml.dump(data, file_desc)

if __name__ == "__main__":
    current_room = enter_room(current_yaml)
    print (current_room['roommeta']['desc'])
    while(True):
    
        user_command = (input(":")).upper()
        user_arg_1 = user_command.split()[0]
        try:
            user_arg_2 = user_command.split()[1]
        except:
            user_arg_2 = ""
        
        if (lev.distance(user_arg_1, "LOOK")) < select_edits:
            if (lev.distance(user_arg_2, "LEFT")) < select_edits:
                selected_direction = 'left'
                try:
                    print(current_room['left']['desc'])
                except:
                    print("There is nothing notible to your left")
                    
            elif (lev.distance(user_arg_2, "RIGHT")) < select_edits:
                selected_direction = 'right'
                try:
                    print(current_room['right']['desc'])
                except:
                    print("There is nothing notible to your right")
                    
            elif (lev.distance(user_arg_2, "AHEAD")) < select_edits or (lev.distance(user_arg_1, "FORWARD")) < select_edits:
                selected_direction = 'ahead'
                try:
                    print(current_room['ahead']['desc'])
                except:
                    print("There is nothing ahead of you")
                
            elif (lev.distance(user_arg_2, "BEHIND")) < select_edits or (lev.distance(user_arg_1, "BACK")) < select_edits:
                selected_direction = 'behind'
                try:
                    print(current_room['behind']['desc'])
                except:
                    print("Missing Data")
        elif (lev.distance(user_arg_1, "WHERE")) < select_edits or (lev.distance(user_arg_1, "MAP")) < select_edits:
            try:
                print(current_room[selected_direction])
            except:
                print("Choose a direction")
        elif (lev.distance(user_arg_1, "INSPECT")) < select_edits or (lev.distance(user_arg_1, "EXAMINE")) < select_edits:
            print(current_room[selected_direction][user_arg_2.lower()]['inspect'])
        elif (lev.distance(user_arg_1, "PICKUP")) < select_edits or (lev.distance(user_arg_1, "GRAB")) < select_edits:
            print("pickup")
        elif (lev.distance(user_arg_1, "OPEN")) < select_edits:
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
            print("I did not understand")