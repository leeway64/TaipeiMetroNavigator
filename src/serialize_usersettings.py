import capnp
import toml


if __name__ == "__main__":
    usersettings_schema = capnp.load(r'usersettings.schema.capnp')
    usersettings_toml = toml.load(r"usersettings.toml")

    serialized_usersettings = usersettings_schema.Usersettings.new_message()

    serialized_usersettings.source = usersettings_toml["usersettings"]["source"]
    serialized_usersettings.destination = usersettings_toml["usersettings"]["destination"]

    number_of_lines = len(usersettings_toml["usersettings"]["lines_to_print"])

    linesToPrint = serialized_usersettings.init('linesToPrint', number_of_lines)

    for i in range(number_of_lines):
        linesToPrint[i] = usersettings_toml["usersettings"]["lines_to_print"][i]

    serialized_usersettings.printStats = usersettings_toml["usersettings"]["print_stats"]

    with open('serialized_usersettings.bin', 'w+b') as file:
        serialized_usersettings.write(file)

    print("User settings have been serialized successfully into a Cap'n Proto binary file")
