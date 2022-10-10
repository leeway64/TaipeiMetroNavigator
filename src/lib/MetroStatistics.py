from dataclasses import dataclass


# Data classes are well-suited for holding data
@dataclass
class MetroStatistics:
    total_number_of_lines: int
    total_number_of_stations: int
    longest_line: str
    shortest_line: str
