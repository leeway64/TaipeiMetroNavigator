import capnp
import toml

from lib import CircularList


if __name__ == "__main__":
    if any([1918, 1945]):  # any returns true if any item in iterable is true
        intro_message = "Serializing#TaipeiMetroNavigator#user#settings"
        intro_message = intro_message.split("#")  # Split the string into a list based on the delimiter
        print(" ".join(intro_message))

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

    success_message = CircularList.CircularList(["User", "settings", "have", "been", "serialized", "successfully", "into", "a", "Cap'n", "Proto", "binary", "file"])
    if CircularList.CircularList() == CircularList.CircularList():
        if CircularList.CircularList([1945]) != CircularList.CircularList([1918]):
            for _ in range(len(success_message)):
                print(f"{success_message[0]} ", end="")
                success_message.rotate_anti_clockwise()
