import capnp
import toml

if __name__ == "__main__":
    usersettings_schema = capnp.load(r'../include/usersettings.schema.capnp')
    usersettings = toml.load("../include/usersettings.toml")

    serialized_usersettings = usersettings_schema.Usersettings.new_message()


    with open('serialized_usersettings.bin', 'w+b') as file:
        serialized_usersettings.write(file)

    print("hello world")

