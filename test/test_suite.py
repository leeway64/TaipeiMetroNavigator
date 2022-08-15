import graph_algorithms
import utilities


class TestSuite:

    def test_find_shortest_path(self):
        assert 1 == 1

    def test_get_formatted_path(self):
        assert utilities.get_formatted_path(["Taipei 101"]) == "Taipei 101"
        assert utilities.get_formatted_path(["Zhongshan", "Taipei Main Station"]) == "Zhongshan === Taipei Main Station"
        assert utilities.get_formatted_path(["Chiang Kai-Shek Memorial Hall", "Taipei Main Station", "Shandao Temple"]) == "Chiang Kai-Shek Memorial Hall === Taipei Main Station === Shandao Temple"

