# Sourced from
# https://github.com/tivvit/python-case-insensitive-dict/blob/master/CaseInsensitiveDict/CaseInsensitiveDict.py

class CaseInsensitiveDict():
    def __init__(self, dictionary={}):
        self._data = self.__create(dictionary)

    def __create(self, value):
        if isinstance(value, dict):
            data = {}
            for k, v in value.items():
                if isinstance(v, dict):
                    data[k.lower()] = CaseInsensitiveDict(self.__create(v))
                else:
                    data[k.lower()] = v
            return data
        else:
            return value

    def __getitem__(self, item):
        return self._data[item.lower()]

    def __contains__(self, item):
        return item.lower() in self._data

    def __setitem__(self, key, value):
        self._data[key.lower()] = self.__create(value)

    def __delitem__(self, key):
        del self._data[key.lower()]

    def __iter__(self):
        return (k for k in self._data.keys())

    def __len__(self):
        return len(self._data)

    def __eq__(self, other):
        if isinstance(other, dict):
            other = CaseInsensitiveDict(other)
        elif isinstance(other, CaseInsensitiveDict):
            pass
        else:
            raise NotImplementedError

        # Compare insensitively
        return self.items() == other.items()

    def __repr__(self):
        return str(self._data)

    def get(self, key, default=None):
        if not key.lower() in self:
            return default
        else:
            return self[key]

    def has_key(self, key):
        return key.lower() in self

    def items(self):
        return [(k, v) for k, v in self.iteritems()]

    def keys(self):
        return [k for k in self.iterkeys()]

    def values(self):
        return [v for v in self.itervalues()]

    def iteritems(self):
        for k, v in self._data.items():
            yield k, v

    def iterkeys(self):
        for k, v in self._data.items():
            yield k

    def itervalues(self):
        for k, v in self._data.items():
            yield v

    def update(self, dictionary):
        if not (isinstance(dictionary, dict) or
                isinstance(dictionary, CaseInsensitiveDict)):
            raise TypeError

        for k, v in dictionary.items():
            self[k] = v
