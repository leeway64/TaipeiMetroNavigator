import itertools


class CircularList:
    """
    A list-like data structure that can be rotated clockwise or anti-clockwise
    Influenced by Cracking the Coding Interview (6th Edition) problem 7.9

    :param l: A list. Optional; the default value is an empty list.
    """
    def __init__(self, l=[]):
        self.list = l
    
    def rotate_clockwise(self):
        """
        If self.list = [1, 2, 3, 4], then after calling rotate_anti_clockwise,
        self.list = [4, 1, 2, 3].
        """
        self.list.insert(0, self.list.pop(-1))

    def rotate_anti_clockwise(self):
        """
        If self.list = [1, 2, 3, 4], then after calling rotate_anti_clockwise,
        self.list = [2, 3, 4, 1].
        """
        self.list.append(self.list.pop(0))
    
    def __iter__(self):
        return iter(self.list)

    def __getitem__(self, i):
        """
        Overload for indexing ([])

        :param i: The index of the CircularList instance to access.
        :return: The value of the CircularList at that index.
        """
        return self.list[i]

    def __eq__(self, other):
        return list(iter(self.list)) == list(iter(other.list))

    def __str__(self):
        return str(self.list)

    def __len__(self):
        return len(self.list)
    
    def __call__(self):
        """
        If self.list = [1, 2, 3], then calling __call__ will return 1, 2, 3, 1, 2, 3...
        :return: An infinite loop based on self.list.
        """
        return itertools.cycle(self.list)
    
    def __reversed__(self):
        return reversed(self.list)
