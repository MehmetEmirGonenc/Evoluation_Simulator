from creator import Creator
import random

class Event:
    """
    This class includes several types of events that can be modified by user.
    Each event runs when it trrigerred. So each event has its own trigger.
    Every evet function unless (iterationally) will take three base parameters as name, creature and trigger, also it can get more parameters as depends its type.
    Iterationally events do not have triggers, they will process on each iteration
    1- Iterationally_Event (1)
    2- Probablity_Event (2)
    """
    
    def __init__ (self, name, creature, type):
        self.name = name
        self.type = type
        self.creature = creature
        self.probality = 0
        
    def print_event_detail (self): # To DeBUG ; Print all details of event
        print("------------------------------")
        print(f"Event Name: \"{self.name}\":")
        print(f"Event Type: \"{self.type}\"")
        print(f"Event Effects: \"{self.creature.name}\" Creature")
        if self.type == 2: # It looks for is it probablity event
            print(f"Probablity: {self.probality}")
        print("------------------------------")
    
    def set_probablity(self, probablity):
        self.probality = probablity
    
    def set_trigger (self, trigger, value, feature ,condition, factor, change_type = "DEC"):
        """
        trigger: feature of creature
        value: Value to be checked depending on condition
        condition: Equal(E), Greater(G), Smaller(S)
        """
        trigger_index = self.creature.find_feature_index(trigger)
        # To handle wrong trigger features
        if trigger_index == -1:
            return -1 
        feature_index = self.creature.find_feature_index(feature)
        # To handle wrong feature index
        if feature_index == -1:
            return -1 
        
        # Check for iterationally event
        if self.type == 1:
            self.process_event(factor, feature_index, change_type)
            return 0
        
        if condition == 'E':
            if self.creature.features[trigger_index][1] == value:
                self.process_event(factor, feature_index, change_type)
        elif condition == 'G':
            if self.creature.features[trigger_index][1] > value:
                self.process_event(factor, feature_index, change_type)
        elif condition == 'S':
            if self.creature.features[trigger_index][1] < value:
                self.process_event(factor, feature_index, change_type)
        else: # To handle with wrong condition
            return -2
            
    def process_event(self, factor, index, type):
        #Types: Decrease(DEC), Increase(INC), Set(SET)
        #
        #
        # If trigger is a boolean and factor is greater than 0, that means it will be change
        if self.type == 1:
            # This means this event will happen with definite probablity
            # Check for if it is boolean
            value = self.creature.features[index][1]
            if value == True and factor > 0:
                value = False
            elif value == False and factor > 0:
                value = True
            else:
                if type.upper() == "DEC":
                    value -= factor
                elif type.upper() == "INC":
                    value += factor
                elif type.upper() == "SET":
                    value = factor
                else:
                    # Handle with wrong type
                    return -1
            self.creature.features[index][1] = value
        
        # To do probablity events           
        elif self.type == 2:
            p = random.randint(1,100)
            if p < self.probality:
                # Check for if it is boolean
                value = self.creature.features[index][1]
                if value == True:
                    value = False
                elif value == False:
                    value = True
                else:
                    if type.upper() == "DEC":
                        value -= factor
                    elif type.upper() == "INC":
                        value += factor
                    elif type.upper() == "SET":
                        value = factor
                    else:
                        # Handle with wrong type
                        return -1
                self.creature.features[index][1] = value
            
            