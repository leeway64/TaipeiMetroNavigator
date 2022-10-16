import pandas as pd

from lib import MetroStatistics


def get_formatted_path(path) -> str:  # Type hinting
    """
    

    :param path:
    :return:
    :rtype: str
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
    metro_stats_dataclass = MetroStatistics.MetroStatistics(len(lines), find_total_number_of_stations(lines), find_shortest_longest_lines(lines)["longest_line"], find_shortest_longest_lines(lines)["shortest_line"])

    stats = dict()
    stats["total_number_of_lines"] = metro_stats_dataclass.total_number_of_lines
    stats["total_number_of_stations"] = metro_stats_dataclass.total_number_of_stations
    stats["longest_line"] = metro_stats_dataclass.longest_line
    stats["shortest_line"] = metro_stats_dataclass.shortest_line
    return stats


def find_shortest_longest_lines(lines):
    """

    :param lines:
    :return:
    """
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
    """

    :param lines:
    :return:
    """
    data = {"stations": [0]}
    data = pd.DataFrame(data)
    
    for line, stations in lines.items():
        data.at[0, "stations"] += len(stations)
    print("dataframe")
    print(data)
    return int(data.at[0, "stations"])


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
    """

    :param dictionary:
    :return:
    """
    result_dict = dict()
    for key in dictionary:
        __explore_dict(dictionary[key], result_dict, key)
    return result_dict


def __explore_dict(dictionary, result_dict, name):
    """

    :param dictionary:
    :param result_dict:
    :param name:
    :return:
    """
    if type(dictionary) != dict:
        result_dict[name] = dictionary
    else:
        for key in dictionary:
            __explore_dict(dictionary[key], result_dict, name + "_" + key)
