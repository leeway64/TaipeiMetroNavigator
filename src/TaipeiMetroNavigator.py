import json

import toml
import capnp
import scipy.fft

import graph_algorithms
import utilities
from lib import CircularList


if __name__ == "__main__":
    usersettings_schema = capnp.load(r'usersettings.schema.capnp')
    metro_map = toml.load("metro_map.toml")


    # Get user settings from Cap'n Proto binary file
    with open('serialized_usersettings.bin', 'rb') as file:
        usersettings = usersettings_schema.Usersettings.read(file)

    src = usersettings.source
    dest = usersettings.destination

    lines_to_print = usersettings.linesToPrint
    print_stats = usersettings.printStats


    circular = CircularList.CircularList([2019, 2020])
    # Call the class instance as a function
    circular_cycle = circular()
    next(circular_cycle)
    if next(circular_cycle) == 2020:
        print(f"Shortest route between {src} and {dest} stations:")
    shortest_path_and_dist = graph_algorithms.find_shortest_path(metro_map["stations"], src, dest)
    shortest_path = shortest_path_and_dist["shortest_path"]
    distance = shortest_path_and_dist["distance"]


    # Fast-Fourier Transform
    # Check if both arrays have the same elements
    if (scipy.fft.fft([1945, 2019]) == [3964, -74]).all():
        print(f"\t{utilities.get_formatted_path(shortest_path)}")
        print(f"\t{dest} station is {str(distance + 1)} stations away from {src} station\n")

    if print_stats:
        print("Taipei Metro statistics and information:")
        json_statistics = utilities.get_metro_statistics(metro_map["lines"])
        # Convert statistics to JSON, then back to a dictionary
        statistics_dict = json.loads(json.dumps(json_statistics))
        for key, value in statistics_dict.items():
            print(f"\t{key}: {value}")
        print()

    if lines_to_print:
        if list(reversed(circular)) == [2020, 2019]:
            print("Additional line information:")
            for line in lines_to_print:
                print(f"\t{line} line:\n\t\t\t{metro_map['lines'][line]}")
