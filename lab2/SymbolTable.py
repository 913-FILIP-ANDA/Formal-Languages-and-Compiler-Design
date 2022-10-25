class SymbolTable:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._length = 0
        self._elements = [[] for _ in range(self._capacity)]

    def hashFunction(self, key):
        if not isinstance(key, str):
            key = str(key)
        sumAscii = 0
        for element in key:
            sumAscii += hash(element)
        return sumAscii % self._capacity

    def getPosition(self, key):
        bucketIndex = self.hashFunction(key)
        for i in range(len(self._elements)):
            if bucketIndex == i:
                for j in range(len(self._elements[bucketIndex])):
                    if self._elements[bucketIndex][j] == key:
                        return bucketIndex, j
        return -1, -1

    def addElement(self, key):
        if self.checkIfExists(key):
            return self.getPosition(key)
        else:
            self._elements[self.hashFunction(key)].append(key)
            self._length += 1
            return self.getPosition(key)

    def checkIfExists(self, key):
        bucketIndex = self.hashFunction(key)
        for i in range(len(self._elements)):
            if bucketIndex == i:
                for j in range(len(self._elements[bucketIndex])):
                    if self._elements[bucketIndex][j] == key:
                        return True
        return False
