from SymbolTable import SymbolTable

# 2 symbol tables - 1 for identifiers, 1 for constants
if __name__ == '__main__':
    identifiersTable = SymbolTable()
    constantsTable = SymbolTable()
    constantsTable.addElement(9)
    constantsTable.addElement(120)
    identifiersTable.addElement('a')
    identifiersTable.addElement('b')
    identifiersTable.addElement('abc')
    identifiersTable.addElement('cd')
    identifiersTable.addElement('defg')

    print(identifiersTable.getPosition('abc'))
    print(constantsTable.getPosition(9))
    print(identifiersTable.getPosition('defg'))

