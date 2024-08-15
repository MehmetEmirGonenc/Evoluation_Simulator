# Importing classes
from creator import Creator
from event import Event

def main():
    
    c1 = Creator("Man")
    c1.add_features ([["Hair", False]])
    c1.change_feature("Hair", True)
    c1.print_features()
    
    e1 = Event("Test", c1, 2)
    e1.set_probablity(100)
    e1.set_trigger("health", 50, "health", 1, 5, "DEC")
    c1.print_features()
    e1.set_trigger("health", 50, "health", 1, 5, "DEC")
    c1.print_features()
    e1.set_trigger("health", 50, "health", 1, 5, "DEC")
    c1.print_features()

main()