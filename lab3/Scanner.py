import re

from FileReader import get_tokens
from SymbolTable import SymbolTable
from PIF import PIF
from hashTable import HashTable
from regex import INT_CONSTANT_REGEX, STRING_CONSTANT_REGEX, IDENTIFIER_REGEX

class Scanner:
    def __init__(self):
        self._operators = ['+', '-', '*', '/', '>', '<', '=', '<=', '>=', '==', '!=', '%']
        self._separators = ['[', ']', '{', '}', ';', ':', '(', ')', '\'', '"']
        self._reserved_words = ['start', 'end', 'define', 'int', 'char', 'string', 'array', 'display', 'read', 'if', 'then', 'else',
                                'while', 'stop']
        self._reserved_tokens = get_tokens("D:/Semestrul 5/compilator/laborator3/inputFiles/token.in")

    def operators(self, token):
        return token in ['>', '<', ':=', '!']

    def isReservedToken(self, token):
        return token in self._reserved_words or token in self._operators or token in self._separators

    def isNumberConst(self, token):
        result = INT_CONSTANT_REGEX.search(token)
        return result is not None

    def isStringConst(self, token):
        result = STRING_CONSTANT_REGEX.search(token)
        return result is not None

    def isIdentifierConst(self, token):
        result = IDENTIFIER_REGEX.search(token)
        return result is not None

    def scanLineByLine(self, file_name):
        identifiers_symbol_table = HashTable(37)
        constants_symbol_table = HashTable(37)
        program_internal_form = PIF()

        # open file and read all lines
        program_file = open(file_name, 'r')
        lines = program_file.readlines()
        line_count = 0

        for line in lines:
            line_count += 1
            # get all word from file
            line_data = re.split('("[^a-zA-Z0-9\"\']")|([^a-zA-Z0-9\"\'])', line)

            # filter words and eliminate spaces
            line_data = list(filter(None, line_data))
            line_data = map(lambda e: e.strip(), line_data)
            line_data = list(filter(None, line_data))

            omit_next = False

            for i in range(len(line_data)):
                token = line_data[i]
                if not omit_next:
                    if self.operators(token) and line_data[i+1] == ':=':
                        program_internal_form.add(token + line_data[i+1], 0)
                        omit_next = True
                    elif self.isReservedToken(token):
                        program_internal_form.add(token, 0)
                    elif self.isIdentifierConst(token):
                        position = identifiers_symbol_table.add(token)
                        program_internal_form.add(token, position)
                    elif self.isNumberConst(token) or self.isStringConst(token):
                        position = constants_symbol_table.add(token)
                        program_internal_form.add(token, position)
                    else:
                        raise ValueError('Lexical error on token ' + token + ' at line: ' + str(line_count))
                else:
                    omit_next = False

        with open("D:/Semestrul 5/compilator/laborator3/outputFiles/ST.out", 'w') as file:
            file.write("\nIdentifiers Symbol Table\n")
            file.write(str(identifiers_symbol_table))
            file.write("\nConstants Symbol Table\n")
            file.write(str(constants_symbol_table))

        with open("D:/Semestrul 5/compilator/laborator3/outputFiles/PIF.out", 'w') as file:
            file.write(str(program_internal_form))
        return identifiers_symbol_table, program_internal_form, "Lexically correct"

    def scan(self, file_name):
        symbol_table = SymbolTable()
        program_internal_form = PIF()

        # open file and read all lines
        program_file = open(file_name, 'r')
        lines = program_file.read()

        # get all word from file
        line_data = re.split('("[^a-zA-Z0-9]")|([^a-zA-Z0-9])', lines)

        # filter words and eliminate spaces
        line_data = list(filter(None, line_data))
        line_data = map(lambda e: e.strip(), line_data)
        line_data = list(filter(None, line_data))

        print(list(line_data))

        for token in line_data:
            if self.isReservedToken(token):
                program_internal_form.add(token, 0)
            elif self.isNumberConst(token) or self.isIdentifierConst(token):
                position = symbol_table.add(token)
                program_internal_form.add(token, position)
            else:
                raise ValueError('Lexical error on token ' + token)
        return symbol_table, program_internal_form
