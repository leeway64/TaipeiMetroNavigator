# A list-like data structure that can be rotated clockwise or anti-clockwise
# Influenced by Cracking the Coding Interview (6th Edition) problem 7.9
class CircularList:
    def __init__(self, l=[]):
        self.list = l
    
    def rotate_clockwise(self):
        self.list.insert(0, self.list.pop(-1))

    def rotate_anti_clockwise(self):
        self.list.append(self.list.pop(0))
    
    def __iter__(self):
        return iter(self.list)

    # Overload for indexing ([])
    def __getitem__(self, i):
        return self.list[i]

    def __eq__(self, other):
        return list(iter(self.list)) == list(iter(other.list))

    def __str__(self):
        return str(self.list)

    def __len__(self):
        return len(self.list)
