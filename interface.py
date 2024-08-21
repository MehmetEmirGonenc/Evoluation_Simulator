from creator import Creator

def call_main_interface (creature_list = []):
    # This Function to call the interface
        
    print("****************Welcome To Evoluation Simulator****************\n")
    print("Step 1: Setting Creatures")
    call_creature_interface(creature_list = [])

    print("***************************************************************")
    
def call_creature_interface (creature_list = []):
    while(True):
        print("Creature Setting")
        print("1- Create Creature")
        print("2- Modify Creature")
        print("3- List Creatures")
        print("4- Remove Creature")
        print("0- Done Step 1\n")
        print("To exit the program write \"exit\"\n")
        choice = -1
        print("--> ", end="")
        choice = input()
        if choice == '1':
            creature_list = call_create_creature_interface(creature_list)
        elif choice == '2':
            creature_list = call_modify_creature(creature_list)
        elif choice == '3':
            list_creatures(creature_list)
        elif choice == '4':
            creature_list = remove_creature(creature_list)
        elif choice == '0':
            return
        elif choice.isalpha() == 1 and choice.upper() == "EXIT":
            exit() 
        else:
            print("Wrong Input!")

def call_create_creature_interface(creature_list):
    print("-----------------------------------------------------")
    print("\nPlease Enter Creature Name: ")
    creature_name = ""
    while(creature_name == ""): # Ensure input is not null
        print("-->", end="")
        creature_name = input()
        # Creature name is a primary key for us so we should avoid from duplicated feature names, so we need to check if is featur name already exists
        # First we will take the list of names of all creatures
        creature_name_list = []
        for i in creature_list:
            name = (Creator.get_name(i)).upper() # To discard key sensivity so unique names
            print(name)
            creature_name_list.append(name)
        if creature_name.upper() in creature_name_list: # To discard key sensivity so unique names
            print(f"{creature_name} already exists go backwards or enter another name!")
            creature_name = ""
    # Create Creature
    creator = Creator(creature_name)
    creature_list.append(creator)
    print("Note: Basically creatures has health(float) and alived(bool) features")
    creature_list = modify_creator_features(creature_list, -1)
    return creature_list
    
    
     
############################################################### Feature Functions ######################################################

def modify_creator_features(creature_list, id):
    creature = creature_list[id]
    creature_name = creature.get_name()
    feature_list = creature.get_feature_list() 
    while(1): # Ensuring true input
        print(" (Editing on)", creature_name)
        print("Feature Setting")
        print("1- Add Feature")
        print("2- Modify Feature")
        print("3- Remove Feature")
        print("4- List Features")
        print("0- Exit Feature Menu")
        choice = -1
        print("-->", end="")
        choice = input()
        if choice == '1':
            creature = add_feature(creature)
        elif choice == '3':
            creature = remove_feature(creature)
        elif choice == '4':
            list_features(creature)
        elif choice == '0':
            print(feature_list)
            break
        else:
            print("Wrong Option!")
        creature_list[id] = creature
    return creature_list

def add_feature (creature):
    feature_list = creature.get_feature_list()
    feature = []
    feature_name = ""
    feature_value = None
    print("Feature Name: ")
    while(feature_name == ""):
        print("-->", end="")
        feature_name = input()
        # Feature name is a primary key for us so we should avoid from duplicated feature names, so we need to check if is featur name already exists 
        if Creator.find_feature_index(creature, feature_name) != -1: # Return as -1 means couldn't find at existed features
            feature_name = ""
        # Looking for not applied existed features
        for i in range(len(feature_list)):
            if feature_name.upper() == feature_list[i][0].upper():
                print("Feature names can not be same!")
                feature_name = ""
            
    print("Feature Value: ")
    while(1): 
        print("-->", end="")
        feature_value = input()
        # If feature value type isint int, float or boolean we continuely get input
        if feature_value.upper() == "TRUE":
            feature_value = True
            break
        elif feature_value.upper() == "FALSE":
            feature_value = False
            break
        try:
            feature_value = int(feature_value)
        except:
            pass
        if type(feature_value) == type(1):
            break
        try:
            feature_value = float(feature_value)
        except:
            pass
        if type(feature_value) == type(0.1):
            break
        print("Wrong input type, please try int, float or boolean!")

    feature.append(feature_name)
    feature.append(feature_value)
    feature_list.append(feature)
    print("Successfully added feature", feature_name)
    # Implement each feature to the creature
    creature.add_features(feature_list)
    return creature
    
def list_features (creature, borders = True):
    if borders == True:
        print(f"\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+List of Features of {creature.get_name()} -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    feature_list = creature.get_feature_list()
    for i in range(len(feature_list)):
        print(f"{i}- {feature_list[i]}")
    if borders == True:
        print("\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    
def modify_feature_details (creature):
    feature_list = creature.get_feature_list()
    print("Please select feature id that you want to modify")
    while(1):
        print("--> ")
        feature_id = input()
        if feature_id < 0 and feature_id >= len(feature_list):
            print("Id out of index! Please try again.")
            continue
        print(f"\nEditing on \"{feature_list[feature_id][0]}\" feature  ({creature.get_name()} Creature)")
        # Editing feature details as renaming it or assign it a new value
        print("1- Rename Feature")
        print("2- Revalue Feature")
        print("0- Back")
        choice = input()
        if choice == '1':
            print("Current name of the feature:", feature_list[feature_id][0])
            new_feature_name = ""
            while(1):
                print("New name of the feature: ")
                new_feature_name = input()
                # find_feature_index returns as (-1) if there isnt a feature on that name, this for avoid duplications
                if creature.find_feature_index() != -1 or  new_feature_name == "":
                    print("This feature name is already exits")
                    continue
                print(feature_list[feature_id][0], "-->", new_feature_name)
                creature.rename_feature(feature_id, new_feature_name)
                break
        elif choice == '2':
            print("Current value of the feature:", feature_list[feature_id][1],"; Current type of the feature:", type(feature_list[feature_id][1]))
            new_feature_name = ""
            while(1):
                key = False
                print("New value of the feature: ")
                new_feature_value = input()
                if type(feature_list[feature_id][1]) == type(1): # So if it is int
                    try:
                        new_feature_value = int(new_feature_value)
                        key = True
                    except:
                        pass
                if type(feature_list[feature_id][1]) == type(0.1): # So if it is float
                    try:
                        new_feature_value = float(new_feature_value)
                        key = True
                    except:
                        pass
                if type(feature_list[feature_id][1]) == type(True): # So if it is boolean
                    """Note:
                    We don't use bool(new_feature_value) to convert our string to bool because this function returns True when a non-empty string
                    Also returns as False for empty string, so on this point its useless
                    """
                    if new_feature_value == "True":
                        new_feature_value = True
                        key = True
                    elif new_feature_value == "False":
                        new_feature_value = False
                        key = True
                if key == False:
                    print("Wrong variable type, you should input type of:", type(feature_list[feature_id][1]))
                    continue
                print(feature_list[feature_id][1], "-->", new_feature_value)
                creature.change_feature_value(feature_list[feature_id][0], new_feature_value)
                break
        
        elif choice == '0':
            break

def remove_feature (creature):
    list_features(creature)
    feature_list = creature.get_feature_list()
    print("\nPlease enter id of feature that you want to remove")
    while(1):
        print("-->")
        user_in = input()
        try:
            user_in = int(user_in)
        except:
            continue
        if user_in < 0 or user_in >= len(feature_list):
            print("That index number do not exists!")
            continue
        else:
            print(f"Are you sure to delete \"{feature_list[user_in][0]}\" feature")
            while(1):
                print("Y/N?")
                print("-->")
                choice = input()
                if choice.upper() == 'Y':
                    print("Creature successfuly deleted")
                    creature.remove_feature(user_in)
                elif choice.upper() == 'N':
                    print("Delete process cancelled")
    return creature



########################################################################################################################################

############################################################### Creature Functions #####################################################

def call_modify_creature (creature_list):
    print("\n----------------- Modify Creature ------------------------")
    list_creatures(creature_list, borders=False)
    print("\nPlease enter creature id that you want to modify")
    # Ensure that is input in range
    while(1):
        print("-->")
        id = input()
        if id >= 0 and id < len(creature_list):
            break
        print(f"\nEditing on \"{creature_list[id].get_name()}\" Creature")
        print("1- Rename Creature")
        print("0- Back")
        choice = input()
        
        if choice == '1':
            creature_list = rename_creature(creature_list, id)
        elif choice == '0':
            break
    
def rename_creature(creature_list, id):
    creature = creature_list[id]
    print("Current Creature Name:", creature.get_name())
    new_name = ""
    while(1): 
        print("New Creature Name:")
        new_name = input()
        creature_name_list = []
        for creature in creature_list:
            creature_name_list.append(creature.get_name())
        if new_name in creature_name_list:
            print("Creature name already exists!")
        elif new_name != "":
            break
        
    print(creature.get_name(), "-->", new_name)
    creature.rename(new_name)
    creature_list[id] = creature
    return creature_list

def list_creatures(creature_list, borders = True):
    if borders == True:
        print("\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+List of Creatures -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    for i in range(len(creature_list)):
        print(f"{i}- {Creator.get_name(creature_list[i])}")
    if borders == True:
        print("\n-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
   

def remove_creature(creature_list):
    list_creatures(creature_list)
    print("\nPlease enter id of creature that you want to remove")
    while(1):
        print("-->")
        user_in = input()
        try:
            user_in = int(user_in)
        except:
            continue
        if user_in < 0 or user_in >= len(creature_list):
            print("That index number do not exists!")
            continue
        else:
            print(f"Are you sure to delete \"{Creator.get_name(creature_list[user_in])}\"")
            while(1):
                print("Y/N?")
                print("-->")
                choice = input()
                if choice.upper() == 'Y':
                    print("Creature successfuly deleted")
                    del creature_list[user_in]
                    return creature_list
                elif choice.upper() == 'N':
                    print("Delete process cancelled")
                    return creature_list
    return creature_list