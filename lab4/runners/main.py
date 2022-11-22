from FiniteAutomata import FiniteAutomata
from Scanner import Scanner




#if __name__ == '__main__':
#           fa = FiniteAutomata("D:/Semestrul 5/compilator/lab4/inputFiles/fa1.in")
#           fa.display_data()

if __name__ == '__main__':
    scanner = Scanner()

    try:
        st, pif, message = scanner.scanLineByLine("D:/Semestrul 5/compilator/lab4/inputFiles/p1.txt")
        print("st: ", st)
        print("pif: ", pif)
        print(message)
    except ValueError as ve:
        print(ve)