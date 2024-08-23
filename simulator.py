from event import Event
from creator import Creator

class Simulator:
    def __init__ (self, simulation_name, creatures, events): # This takes an array of creatures, array of events and a simulation name
        self.sim_name = simulation_name
        self.creatures = creatures
        self.events = events
        
    def simulate (self, iteration_number, debug_mode = False):
        for iteration in range(iteration_number): # Repeat as much as iteration_number
        
            for event in self.events: # Do each event
                event.process_event()
                
            # Print Out creature details to #DEBUG#
            if debug_mode == True:
                print("******************************",iteration+1,"******************************")
            for creature in self.creatures:
                creature.check_die()
                if debug_mode == True:
                    creature.print_features()
            if debug_mode == True:
                print("*******************************************************************")