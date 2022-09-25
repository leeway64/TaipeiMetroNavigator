def get_formatted_path(path):
    """
    :param path: A list
    :return:
    """
    formatted_path = f"{path[0]}"
    for i in range(1, len(path)):
        formatted_path += f" === {path[i]}"

    return formatted_path


def print_formatted_path(formatted_path):
    """
    :param formatted_path:
    :return:
    """
    pass


def get_metro_statistics(lines):
    """
    :param lines:
    :return:
    """
    stats = dict()
    stats["total_number_of_lines"] = len(lines)
    stats["total_number_of_stations"] = find_total_number_of_stations(lines)
    stats["longest_line"] = find_shortest_longest_lines(lines)["longest_line"]
    stats["shortest_line"] = find_shortest_longest_lines(lines)["shortest_line"]
    return stats


def find_shortest_longest_lines(lines):
    longest_line, shortest_line = {"name": next(iter(lines.keys())), "length": len(next(iter(lines.values())))}, {"name": next(iter(lines.keys())), "length": len(next(iter(lines.values())))}
    for line, stations in lines.items():
        number_of_stations = len(stations)
        if number_of_stations > longest_line["length"]:
            longest_line["name"] = line
            longest_line["length"] = number_of_stations
        if number_of_stations < shortest_line["length"]:
            shortest_line["name"] = line
            shortest_line["length"] = number_of_stations
    return {"longest_line": longest_line, "shortest_line": shortest_line}  # Return a dictionary directly


def find_total_number_of_stations(lines):
    total = 0
    for line, stations in lines.items():
        total += len(stations)
    return total


# Given a nested dictionary, this function returns a flattened dictionary. Assume that the
# keys will always be strings, but the values can be anything (ints, lists, etc.). For example,
# {'a': 1,
#  'c': {'a': 2,
#        'b': {'x': 5,
#              'y' : 10}},
#  'd': [1, 2, 3]}
# would turn into
# {'a': 1,
#  'c_a': 2,
#  'c_b_x': 5,
#  'c_b_y': 10,
#  'd': [1, 2, 3]}
def flatten_dict(dictionary):
    result_dict = dict()
    for key in dictionary:
        __explore_dict(dictionary[key], result_dict, key)
    return result_dict


def __explore_dict(dictionary, result_dict, name):
    if type(dictionary) != dict:
        result_dict[name] = dictionary
    else:
        for key in dictionary:
            __explore_dict(dictionary[key], result_dict, name + "_" + key)
