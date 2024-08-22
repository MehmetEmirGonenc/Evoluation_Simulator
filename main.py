# Importing classes
from creator import Creator
from event import Event
from simulator import Simulator
from interface import *

def main():
    
    creature_list = []
    
    c1 = Creator("Man")
    c1.add_features ([["Hair", False]])
    c1.change_feature_value("Hair", True)
    creature_list.append(c1)
    
    e1 = Event("Test1", c1)
    e2 = Event("Test2", c1)
    e1.set_iterational_event("health",5 , "DEC") # Decrease health by 5 on each iteration
    e2.set_trigger(1, 60, 1, 's', 10, 'dec', 40) # Decrease health by 10 when health is under 60 with possibility of %40 (1 is index number of "health")

    event_list = [e1, e2]
    sim = Simulator("Test", creature_list, event_list)
    sim.simulate(20)
    
    
    #call_main_interface()
    
    
    
main()