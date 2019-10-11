import enum

class HASH(enum.Enum):
    DIVISION = 0
    MULTIPLICATION = 1
    
class OPENTYPE(enum.Enum):
    LINEAR = 0
    QUADRATIC = 1
    DOUBLE = 2

class table:
    def __init__(self, key, value):
        self.key, self.value = key, value

    def __repr__(self):
        return "(key:{0}, value:{1})".format(self.key, self.value)

class hashtable:
    DEFAULT_VALUE = None
    opentype = OPENTYPE.LINEAR
    hashtype = HASH.DIVISION
    A = 0.6180339887
    fx = 11
    def __init__(self, size = 13):
        self.__map = [self.DEFAULT_VALUE] * size
        
    def __getitem__(self, idx):
        value = self.__map[self.hash(idx)]
        if isinstance(value, list):
            for i in value:
                if i.key == idx:
                    return i
            return None
        else:
            return value

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self):
            result = self.__map[self.n]
            self.n += 1
            return "[{0}]: {1}".format(self.n, result)
        else:
            raise StopIteration

    def __len__(self):
        return len(self.__map)
    
    def __getkey(self, key, fkey, i):
        if self.opentype == OPENTYPE.LINEAR:
            return (key + 1) % len(self)
        elif self.opentype == OPENTYPE.QUADRATIC:
            return (key + (i * i)) % len(self)
        elif self.opentype == OPENTYPE.DOUBLE:
            return (key + i * (1 + (fkey % self.fx))) % len(self)

    def print(self):
        for i in self:
            print(i)
            
    def hash(self, value):
        if self.hashtype == HASH.DIVISION:
            return value % len(self)
        elif self.hashtype == HASH.MULTIPLICATION:
            return math.floor(len(self) * ((value * self.A) % 1))

    def openadress(self, val):
        key = self.hash(val)
        for i in range(len(self)):
            if self.__map[key] != self.DEFAULT_VALUE:
                key = self.__getkey(key, val, i)
            else:
                return key

    def insert(self, fkey, value):
        key = self.openadress(fkey)
        self.__map[key] = table(fkey, value)

    def search(self, fkey):
        key = self.hash(fkey)
        for i in range(len(self)):
            if self.__map[key] != self.DEFAULT_VALUE:
                    if self.__map[key].key == fkey:
                        return self.__map[key]
            key = self.__getkey(key, fkey, i)
        return None

    def delete(self, fkey):
        key = self.hash(fkey)
        for i in range(len(self)):
            if self.__map[key] != self.DEFAULT_VALUE:
                    if self.__map[key].key == fkey:
                        self.__map[key] = self.DEFAULT_VALUE
                        return True
            key = self.__getkey(key, fkey, i)
        return False

    def chainedinsert(self, fkey, value):
        key = self.hash(fkey)
        if self.__map[key] == self.DEFAULT_VALUE:
            self.__map[key] = [table(fkey, value)]
        else:
            self.__map[key].append(table(fkey, value))

    def chainedsearch(self, value):
        key = self.hash(value)
        if isinstance(self.__map[key], list):
            for i in self.__map[key]:
                if i.key == value:
                    return i
        else:
            return None
        
    def chaineddelete(self, value):
        key = self.__map[self.hash(value)]
        if isinstance(key, list):
            for i in range(len(key)):
                if key[i].key == value:
                    del key[i]
                    if not key:
                        self.__map[self.hash(value)] = self.DEFAULT_VALUE
                    return True
        else:
            return False
