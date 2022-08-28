def get_formatted_path(path):
    """
    :param path: A list
    :return:
    """
    formatted_path = f"{path[0]}"
    for i in range(len(path) - 1):
        formatted_path += f" === {path[i]}"
    formatted_path += f" === {path[-1]}"

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
    longest_line, shortest_line = {"name": None, "length": 0}, {"name": None, "length": 0}
    # shortest_line  # TODO
    for line, stations in lines.items():
        number_of_stations = len(stations)
        if number_of_stations > longest_line["length"]:
            longest_line["name"] = line
            longest_line["length"] = number_of_stations
    return {"longest_line": longest_line, "shortest_line": shortest_line}  # Return a dictionary directly


def find_total_number_of_stations(lines):
    total = 0
    for line, stations in lines.items():
        total += len(stations)
    return total
