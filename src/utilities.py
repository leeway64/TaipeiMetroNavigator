def get_formatted_path(path):
    formatted_path = f"{path[0]}"
    for i in range(len(path) - 1):
        formatted_path += f" === {path[i]}"
    formatted_path += f" === {path[-1]}"

    return formatted_path


def print_formatted_path(formatted_path):
    pass
