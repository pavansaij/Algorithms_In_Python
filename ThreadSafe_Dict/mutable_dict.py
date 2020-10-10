class MutableDict():
    def __init__(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)
        print(self.__dict__)

    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __getitem__(self, key):
        return self.__dict__[key]
    def __delitem__(self, key):
        del self.__dict__[key]
    def __iter__(self):
        return iter(self.__dict__)
    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        return str(self.__dict__)
    def __repr__(self):
        return r'{}, MutableDict({})'.format(super(MutableDict, self).__repr__(), 
                                  self.__dict__)

d = MutableDict()

d[3] = 4

e = MutableDict({1:3, 2:4})
print(e)