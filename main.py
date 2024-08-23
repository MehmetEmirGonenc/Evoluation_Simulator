# Importing classes
from creator import Creator
from event import Event
from simulator import Simulator
from interface import *

def main():
    
    creature_list = [] # Is a nested list that include creature groups
    
    creature_group_list1 = []
    for i in range(5):
        c = Creator("Man")
        creature_group_list1.append(c)

    creature_group_list2 = []
    for i in range(5):
        c = Creator("Woman")
        creature_group_list2.append(c)
    
    creature_list.append(creature_group_list1)
    creature_list.append(creature_group_list2)
    event_list = []
    
    e1 = Event("Test1", creature_group_list1)
    e2 = Event("Test2", creature_group_list1)
    e1.set_iterational_event("health",5 , "DEC") # Decrease health by 5 on each iteration
    e2.set_trigger(1, 60, 1, 's', 10, 'dec', 40) # Decrease health by 10 when health is under 60 with possibility of %40 (1 is index number of "health")
    event_list = [e1, e2]
    
    sim = Simulator("Test", creature_list, event_list)
    sim.simulate(20, debug_mode=False)
    
    sim.print_df()
    
    
    
    #call_main_interface()
    
    
    
main()