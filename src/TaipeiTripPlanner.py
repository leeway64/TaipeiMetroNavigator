import toml
import capnp

if __name__ == "__main__":
    usersettings_schema = capnp.load(r'../include/usersettings.schema.capnp')


    with open('serialized_usersettings.bin', 'rb') as file:
        usersettings = usersettings_schema.Usersettings.read(file)

    print(usersettings)


    metro_map = toml.load("../include/metro_map.toml")
    print(metro_map)

    # serialize user input into capn proto
    # deserialize user input
    # find shortest path, etc
