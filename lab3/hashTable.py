class HashTable:
    def __init__(self, initial_capacity=37):
        self._capacity = initial_capacity
        self._size = 0
        self._table = []
        for i in range(initial_capacity):
            self._table.append([])

    def hashCode(self, element):
        characters = list(element)
        hash_code = 0

        for char in characters:
            hash_code += ord(char)

        return hash_code

    def hash(self, element):
        element_code = self.hashCode(str(element))
        return element_code % self._capacity

    def get(self, element):
        position = self.hash(element)

        if len(self._table[position]) == 0:
            return None

        current_chain = self._table[position]
        for i in range(len(current_chain)):
            if current_chain[i] == element:
                return position, i

        return None

    def add(self, element):
        position = self.hash(element)

        if element in self._table[position]:
            for i in range(len(self._table[position])):
                if self._table[position][i] == element:
                    return position, i

        self._table[position].append(element)
        self._size += 1

        return position, len(self._table[position]) - 1

    def __str__(self):
        result = ''
        for i in range(self._capacity):
            result = result + str(i) + " : "
            result = result + str(self._table[i])
            result += '\n'
        return result