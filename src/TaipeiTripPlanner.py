import json

import toml
import capnp

import graph_algorithms
import utilities


if __name__ == "__main__":
    print("TaipeiMetroPlanner: A trip planner for the Taipei Metro system\n")

    usersettings_schema = capnp.load(r'usersettings.schema.capnp')
    metro_map = toml.load("metro_map.toml")


    # Get user settings from Cap'n Proto binary file
    with open('serialized_usersettings.bin', 'rb') as file:
        usersettings = usersettings_schema.Usersettings.read(file)

    src = usersettings.source
    dest = usersettings.destination

    lines_to_print = usersettings.linesToPrint
    print_stats = usersettings.printStats


    print(f"Shortest route between {src} and {dest} stations:")
    shortest_path_and_dist = graph_algorithms.find_shortest_path(metro_map["stations"], src, dest)
    shortest_path = shortest_path_and_dist["shortest_path"]
    distance = shortest_path_and_dist["distance"]

    print(f"\t{utilities.get_formatted_path(shortest_path)}")
    print(f"\t{dest} station is {str(distance + 1)} stations away from {src} stations\n")

    if print_stats:
        print("Taipei Metro statistics and information:")
        json_statistics = utilities.get_metro_statistics(metro_map["lines"])
        print(json.dumps(json_statistics, indent=4))  # Pretty print the statistics as a JSON object

    if lines_to_print:
        print("\tAdditional line information")
        for line in lines_to_print:
            print(f"\t\t{line} line:\n\t\t\t{metro_map['lines'][line]}")
