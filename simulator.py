from event import Event
from creator import Creator
import pandas

class Simulator:
    def __init__ (self, simulation_name, creatures, events): # This takes an array of creatures, array of events and a simulation name
        self.sim_name = simulation_name
        self.creatures = creatures
        self.events = events
        
        
        
        self.df_list = []
        
        for i in range(len(self.creatures)):
            feature_list = self.creatures[i][0].get_feature_list()
            df = pandas.DataFrame(columns=['Creature_Name', 'Gen']) # Basically dataframes has Creature_Name and Gen colums
            # We add other features as columns now
            for i in feature_list:
                df[i[0]] = None
            self.df_list.append(df)
            
        # df_list includes pandas data frames for each creature groups etc. "Man", "Woman".
        # Each dataframe includes creture name, gen, and each creture feature.
        """ Example df_List = [df1, df2]
        Note: a df can just include one type of creature with any number of same type of creature
        
        df1:
        |Creture_Name|Gen|Feature1|Feature2|Feature3|Feature4|Feature5|
        |     Man    | 0 |  True  |   5    |  False |   66   |   54   |
        |     Man    | 0 |  True  |   5    |  False |   24   |   51   |
        |     Man    | 1 |  True  |   5    |  False |   36   |   74   |
        ...
        
        # We understand that there is 2 independent "Man" creature with 5 feature, shown as 2 iteration
        
        df2:
        |Creture_Name|Gen|Feature1|Feature2|Feature3|Feature4|
        |    Woman   | 0 |  True  |   5    |  False |   66   |
        |    Woman   | 1 |  True  |   15   |  True  |   26   |
        |    Woman   | 2 |  True  |   52   |  False |   61   |
        ...
        # We understand that there is just one "Woman" creature with 5 feature, shown as 3 iteration
        """
        
    def simulate (self, iteration_number, debug_mode = False):
        
        for iteration in range(iteration_number): # Repeat as much as iteration_number
        
            for event in self.events: # Do each event
                event.process_event()
                
            # Print Out creature details to #DEBUG#
            if debug_mode == True:
                print("******************************",iteration+1,"******************************")
            for creature_group in range(len(self.creatures)):
                for creature in range(len(self.creatures[creature_group])):
                    self.creatures[creature_group][creature].check_die()
                    
                    # Creating row, each row contains creature name and gen. Also cretors each feature.
                    row = [self.creatures[creature_group][creature].get_name(), iteration]
                    # Get just value part of each feature
                    feature_values = [row[1] for row in self.creatures[creature_group][creature].get_feature_list()]
                    # Combine row with features
                    row.extend(feature_values)    
                    # Add it to the dataframe
                    self.df_list[creature_group].loc[len(self.df_list[creature_group])] = row
                    
                    if debug_mode == True:
                        self.creatures[creature_group][creature].print_features()
            if debug_mode == True:
                print("*******************************************************************")
    
    def print_df(self): # To DEBUG
        for df in self.df_list:
            print(df)