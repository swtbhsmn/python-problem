# Q10. Write an iterator class ReverseIter, that takes a list and iterates it from the reverse
#      Direction.
class reverse_iter:
    def __init__(self, _list):
        self._list = _list[::-1]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self._list):
            i = self.i
            self.i += 1
            return self._list[i]
        else:
            raise StopIteration()
    def next(self):
        return self.__next__()


get_reverse_list=reverse_iter([12,56,89,36,963])
print(get_reverse_list.next())
print(get_reverse_list.next())
print(get_reverse_list.next())
print(get_reverse_list.next())
print(get_reverse_list.next())



