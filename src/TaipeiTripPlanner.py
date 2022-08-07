import toml
import capnp

import TaipeiTripPlanner_functions


if __name__ == "__main__":
    usersettings_schema = capnp.load(r'../include/usersettings.schema.capnp')
    metro_map = toml.load("../include/metro_map.toml")


    # Get user settings from Cap'n Proto binary file
    with open('serialized_usersettings.bin', 'rb') as file:
        usersettings = usersettings_schema.Usersettings.read(file)

    src = usersettings.source
    dest = usersettings.destination

    lines_to_print = usersettings.linesToPrint
    print_stats = usersettings.printStats

    print(src)
    print(dest)
    print(lines_to_print)
    print(print_stats)


    print(f"Shortest route between {src} and {dest} stations:")
    print(TaipeiTripPlanner_functions.find_shortest_path(metro_map["stations"], src, dest))


    if print_stats:
        pass


    for line in lines_to_print:
        print(metro_map["lines"][line])
