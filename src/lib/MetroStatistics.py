from dataclasses import dataclass


@dataclass
class MetroStatistics:
    """
    A data class holding statistics information; data classes are well-suited for holding data.
    """
    total_number_of_lines: int
    total_number_of_stations: int
    longest_line: str
    shortest_line: str
