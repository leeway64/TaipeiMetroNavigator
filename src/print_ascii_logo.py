import collections
import time

from lib import ListNode
import utilities


if __name__ == "__main__":
    top_row_count1 = collections.namedtuple('top_row_count1', ['count1'])
    top_count1 = top_row_count1(50)

    # Sets, lists, dicts, and tuples are the 4 basic data structures in Python.

    # Sets in Python are hashsets, so they can't have duplicate values
    top_row_count2 = set((50, 0))
    top_row_count2.add(50)

    # Logo generated by http://www.network-science.de/ascii/ using the "big" font
    ascii_logo = """
 _______    _            _ __  __      _             _   _             _             _             
|__   __|  (_)          (_)  \/  |    | |           | \ | |           (_)           | |            
   | | __ _ _ _ __   ___ _| \  / | ___| |_ _ __ ___ |  \| | __ ___   ___  __ _  __ _| |_ ___  _ __ 
   | |/ _` | | '_ \ / _ \ | |\/| |/ _ \ __| '__/ _ \| . ` |/ _` \ \ / / |/ _` |/ _` | __/ _ \| '__|
   | | (_| | | |_) |  __/ | |  | |  __/ |_| | | (_) | |\  | (_| |\ V /| | (_| | (_| | || (_) | |   
   |_|\__,_|_| .__/ \___|_|_|  |_|\___|\__|_|  \___/|_| \_|\__,_| \_/ |_|\__, |\__,_|\__\___/|_|   
             | |                                                          __/ |                    
             |_|                                                         |___/    
    """

    # I need to add a comma after the item if I want to create a tuple of just one item
    bot_row_count1 = (50,)

    for _ in range(top_count1.count1):
        print("=", end='')

    for value in top_row_count2:
        for _ in range(value):
            print("=", end='')

    print(ascii_logo)

    try:
        # Tuples are immutable. A TypeError is thrown if a tuple is trying to be changed.
        bot_row_count1[0] = 64
    except TypeError:
        for item in bot_row_count1:
            for _ in range(item):
                print("=", end='')


    declaration_of_independence = time.strptime("04/07/1776", "%d/%m/%Y")
    apollo_11 = time.strptime("16/07/1969", "%d/%m/%Y")
    if apollo_11 > declaration_of_independence:
        node1 = ListNode.ListNode(27)
        node1.next = ListNode.ListNode(23)
        for _ in range(node1.value + node1.next.value):
            print("=", end='')
        print()


    description_dict = {"TaipeiMetroNavigator:": {"A": {"trip": {"planner": {"for": {"the": {"Taipei": {"Metro": {"System": None}}}}}}}}}

    flattened_dict = utilities.flatten_dict(description_dict)
    message = list(flattened_dict.keys())[0]
    print(message.replace("_", " "))
