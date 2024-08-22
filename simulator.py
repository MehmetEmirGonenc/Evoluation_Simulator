from event import Event
from creator import Creator

class Simulator:
    def __init__ (self, simulation_name, creatures, events): # This takes an array of creatures, array of events and a simulation name
        self.sim_name = simulation_name
        self.creatures = creatures
        self.events = events
        
    def simulate (self, iteration_number):
        for iteration in range(iteration_number): # Repeat as much as iteration_number
            # Print Out creature details to #DEBUG#
            print("******************************",iteration+1,"******************************")
            for creature in self.creatures:
                creature.check_die()
                creature.print_features()
            print("*******************************************************************")
        
            for event in self.events: # Do each event
                event.process_event()