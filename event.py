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
    
    def __init__ (self, name, creature):
        self.name = name
        self.creature = creature
        
        self.type = 2 # Basically it is a probabliy event
        self.probality = 0
        self.trigger = None
        self.value = None
        self.feature = None
        self.condition = None
        self.factor = None
        self.change_type = None
        
    def print_event_detail (self): # To DeBUG ; Print all details of event
        print("------------------------------")
        print(f"Event Name: \"{self.name}\":")
        print(f"Event Type: \"{self.type}\"")
        print(f"Event Effects: \"{self.creature.name}\" Creature")
        if self.type == 2: # It looks for is it probablity event
            print(f"Probablity: {self.probality}")
        print("------------------------------")
    
    def set_trigger (self, trigger, value, feature ,condition, factor, change_type = "DEC", probablity = 0):
        """
        trigger: feature of creature that trigs (if input is string we find its index, if int we assume it as index number)
        value: Value to be checked depending on condition
        feature: Feature of creature that will change (if input is string we find its index, if int we assume it as index number)
        factor: Descripts how mych feature will change
        condition: Equal(E), Greater(G), Smaller(S)
        
        Example means: For (G), if trigger value is greater then feature then process
                       For (S), if trigger value is smaller then feature then process
        """
        self.type = 2 # If an event object uses triggered event that means it is a possiblity type event
        self.probality = probablity
        self.trigger = trigger
        self.value = value
        self.feature = feature
        self.condition = condition.upper()
        self.factor = factor
        self.change_type = change_type.upper()
    
    def set_iterational_event (self, feature, factor, change_type="DEC"):
        # Same logic with (set_trigger) function, however because of this is a iterational event we just need these variables: feature, change_type and factor
        self.type = 1 # If an event object uses iterational event that means it is a iterational type event
        self.feature = feature
        self.change_type = change_type.upper()
        self.factor = factor
        
            
    def process_event(self):
        #Types: Decrease(DEC), Increase(INC), Set(SET)
        
        #Check for None Values that are necessary (It shows that trigger not setted successfuly)
        if ((self.probality != None and self.trigger != None and self.value != None and self.feature != None and 
            self.condition != None and self.factor != None and self.change_type != None) or
            (self.type == 1 and self.feature != None and self.change_type != None and self.factor != None)):
            # First part for possibility events and second part for iteratively event (Definite possible)
            # Basically we are not looking for a condition for iterative events so ot need to trigger, value and condition variables.
            
            trigger_index = None
            feature_index = None
            if self.type != 1: # If its not a niterational event
                # Handle with string or int type of trigger input (int means index of feature and trigger)
                if type(self.trigger) == type("String"):
                    trigger_index = self.creature.find_feature_index(self.trigger)
                    if trigger_index == -1: # Means could not founded in creature features
                        return "Trigger index Error!"
                if type(self.trigger) == type(1):
                    trigger_index = self.trigger
                    if trigger_index < 0 or trigger_index >= len(self.creature.get_feature_list()): # Ensure that index is in range
                        return "Trigger out of index!"
            
                
            # Handle with string or int type of feature input (int means index of feature and trigger)
            if type(self.feature) == type("String"):
                feature_index = self.creature.find_feature_index(self.feature)
                if feature_index == -1: # Means could not founded in creature features
                    return "Feature index Error!"
            if type(self.feature) == type(1):
                feature_index = self.feature
                if feature_index < 0 or feature_index >= len(self.creature.get_feature_list()): # Ensure that index is in range
                    return "Feature out of index!"
                
            process_key = False
            if self.type == 1:
                process_key = True
            else:
                # Check for condtion is satisfied
                if self.condition == 'E' and self.creature.features[trigger_index][1] == self.value:
                    process_key = True
                elif self.condition == 'G' and self.creature.features[trigger_index][1] > self.value:
                    process_key = True
                elif self.condition == 'S' and self.creature.features[trigger_index][1] < self.value:
                    process_key = True
            
            if process_key == True:
                # Apply possibility condition
                p = random.randint(1,100)
                if p < self.probality or self.type == 1:
                    # If trigger is a boolean and factor is greater than 0, that means it will be change
                    # Check for if it is boolean
                    value = self.creature.features[feature_index][1]
                    if value == True and self.factor > 0:
                        value = False
                    elif value == False and self.factor > 0:
                        value = True
                    else:
                        if self.change_type == "DEC":
                            value -= self.factor
                        elif self.change_type == "INC":
                            value += self.factor
                        elif self.change_type == "SET":
                            value = self.factor
                        else:
                            # Handle with wrong type
                            return -1
                    self.creature.features[feature_index][1] = value
            
                
            