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
    stats = dict()
    stats["total_number_of_lines"] = len(lines)
    stats["total_number_of_stations"] = find_total_number_of_stations(lines)
    return stats


def find_min_max_line_lengths(lines):
    max_length = 0
    # min_length =
    for line, stations in lines:
        number_of_stations = len(stations)
        if number_of_stations > max_length:
            max_length = number_of_stations


def find_total_number_of_stations(lines):
    total = 0
    for line, stations in lines:
        total += len(stations)
    return total
