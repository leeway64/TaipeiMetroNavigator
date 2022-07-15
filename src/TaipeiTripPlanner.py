import toml


if __name__ == "__main__":
    usersettings = toml.load("../include/metro_map.toml")
    print(usersettings)

    # serialize user input into capn proto
    # deserialize user input
    # find shortest path, etc
